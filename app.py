from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from caption_generator import CaptionGenerator

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Ensure API key is available from environment
if not os.getenv('ANTHROPIC_API_KEY'):
    raise ValueError("ANTHROPIC_API_KEY environment variable is required")

# Initialize generator
generator = CaptionGenerator()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Caption Generator API is running"})

@app.route('/generate', methods=['POST'])
def generate_content():
    """Generate Instagram caption and YouTube title from script"""
    try:
        # Get script from request
        data = request.get_json()
        if not data or 'script' not in data:
            return jsonify({"error": "Script is required"}), 400
        
        script = data['script'].strip()
        if not script:
            return jsonify({"error": "Script cannot be empty"}), 400
        
        # Generate content
        result = generator.generate_content(script)
        
        # Return results with additional metadata
        response = {
            "success": True,
            "data": {
                "instagram_caption": result["instagram_caption"],
                "youtube_title": result["youtube_title"],
                "youtube_title_length": len(result["youtube_title"]),
                "hashtag_count": result["youtube_title"].count('#'),
                "word_count": len(result["instagram_caption"].split()),
                "script_length": len(script)
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/analyze-crux', methods=['POST'])
def analyze_crux():
    """Analyze and return just the crux element from script"""
    try:
        data = request.get_json()
        if not data or 'script' not in data:
            return jsonify({"error": "Script is required"}), 400
        
        script = data['script'].strip()
        if not script:
            return jsonify({"error": "Script cannot be empty"}), 400
        
        # Get crux analysis
        crux_data = generator.identify_crux(script)
        
        return jsonify({
            "success": True,
            "data": crux_data
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Starting Caption Generator API...")
    print("📋 Available endpoints:")
    print("  - GET  /health          - Health check")
    print("  - POST /generate        - Generate content")
    print("  - POST /analyze-crux    - Analyze crux only")
    
    port = int(os.environ.get('PORT', 5001))
    print(f"🌐 API running on port {port}")
    
    app.run(debug=False, host='0.0.0.0', port=port)