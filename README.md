# Instagram Caption & YouTube Title Generator

A Python 3 application that generates Instagram captions and YouTube titles from video script inputs using Claude API (Sonnet 4) for dynamic, niche-adaptive content processing.

## Features

- **Dynamic Crux Identification**: Uses Claude API to identify specific tools, concepts, or unique angles from any niche
- **Prompt-Based Processing**: No fixed pillars - adapts to any content type or niche
- **Instagram Caption Generation**: 150-300 words with proper formatting, keywords, and hashtags
- **YouTube Title Generation**: Under 55 characters with exactly 2 hashtags
- **Niche Agnostic**: Works with any type of content (business, psychology, tech, etc.)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Anthropic API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

## Usage

### Basic Usage

```python
from caption_generator import CaptionGenerator

# Initialize generator
generator = CaptionGenerator()

# Generate content from script
script = "Your video script text here..."
result = generator.generate_content(script)

print("Instagram Caption:")
print(result["instagram_caption"])

print("YouTube Title:")
print(result["youtube_title"])
```

### With Custom API Key

```python
generator = CaptionGenerator(api_key="your-api-key")
```

## Testing

Run the test script to validate functionality:

```bash
python test_generator.py
```

This will test the generator with the provided example scripts and validate:
- Crux identification accuracy
- Instagram caption formatting
- YouTube title character limits
- Hashtag requirements

## Output Format

The generator returns a dictionary with:

```python
{
    "instagram_caption": "Full formatted caption with crux definition start, bridge paragraph, CTA, [keywords], and #hashtags",
    "youtube_title": "Title Under 55 Chars #Tag #Tag"
}
```

## Instagram Caption Structure

1. **Hook Paragraph (2-3 sentences)**: Starts with crux definition
2. **Connection Paragraph (3-4 sentences)**: Bridges crux to main message
3. **Call-to-Action (1 sentence)**: Actionable, relevant CTA
4. **Keywords**: [10 keywords, comma-separated]
5. **Hashtags**: 15 relevant hashtags

## YouTube Title Requirements

- Maximum 55 characters including hashtags
- Exactly 2 hashtags
- Hook-focused for curiosity/urgency
- Specific numbers or outcomes when possible

## Crux Identification

The system identifies specific, tangible elements from scripts:
- Specific tools (Apollo, Cursor AI, etc.)
- Specific methods (Dale Carnegie method, etc.)
- Specific concepts (Algorithm, Web scraping, etc.)
- Technical frameworks mentioned

**NOT** the main theme - focuses on supporting elements that can be defined independently.

## API Requirements

- Anthropic API key with access to Claude 3.5 Sonnet
- Internet connection for API calls
- JSON response parsing capability

## Error Handling

The application includes comprehensive error handling for:
- Missing API keys
- Invalid scripts
- API failures
- JSON parsing errors
- Character limit violations

## Dependencies

- `anthropic>=0.34.0` - Claude API client

## License

This project follows the specifications provided in the attached .md file for Instagram caption and YouTube title generation.