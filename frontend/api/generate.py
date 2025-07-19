from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Add the current directory to the path to import caption_generator
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from caption_generator import CaptionGenerator

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Ensure API key is available from environment
            if not os.environ.get('ANTHROPIC_API_KEY'):
                self.send_error(500, "ANTHROPIC_API_KEY environment variable is required")
                return
                
            # Initialize generator
            generator = CaptionGenerator()
            
            # Get request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Validate input
            if not data or 'script' not in data:
                self.send_error(400, "Script is required")
                return
                
            script = data['script'].strip()
            if not script:
                self.send_error(400, "Script cannot be empty")
                return
            
            # Generate content
            result = generator.generate_content(script)
            
            # Prepare response
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
            
            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            error_response = {
                "success": False,
                "error": str(e)
            }
            self.wfile.write(json.dumps(error_response).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()