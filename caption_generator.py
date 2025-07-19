import os
import json
from typing import Dict, Optional
import anthropic
from anthropic import Anthropic


class CaptionGenerator:
    """
    Instagram Caption & YouTube Title Generator using Claude API
    
    Dynamically generates content using Claude Sonnet 4 for adaptive processing
    across different niches and script types.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the caption generator with Claude API
        
        Args:
            api_key: Anthropic API key (if not provided, will use ANTHROPIC_API_KEY env var)
        """
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is required or pass api_key parameter")
        
        self.client = Anthropic(api_key=self.api_key)
        
        # System prompt for crux identification
        self.crux_prompt = """You are an expert content analyst. Your task is to identify the "crux" element from a video script.

The crux is a specific, tangible element mentioned in the script that can be defined or explained, NOT the main overarching message.

Examples of good crux elements:
- Specific tools: "Claude Code", "Apollo", "Cursor AI"
- Specific methods: "Dale Carnegie School method", "Web scraping"
- Specific concepts: "The algorithm", "Content curation"
- Specific techniques or frameworks mentioned

DO NOT choose:
- The main theme or message of the script
- Generic concepts like "success" or "growth"
- Broad topics like "AI" or "business"

Look for:
1. Specific tools, methods, or systems mentioned
2. Concrete examples or case studies referenced  
3. Technical concepts or frameworks that can be defined
4. Something that can be explained independently but connects to the main message

If no clear crux exists, create one from a specific aspect of the topic.

Respond with ONLY a JSON object containing:
{
  "crux_concept": "Name of the crux element",
  "crux_definition": "Clear definition/explanation of this element in 1-2 sentences"
}"""

        # System prompt for Instagram caption generation
        self.instagram_prompt = """You are an expert Instagram caption writer. Generate a caption following these EXACT specifications:

FORMAT REQUIREMENTS:
- 150-300 words total
- Hook Paragraph (2-3 sentences): Start with the crux definition, then add supporting context
- Connection Paragraph (3-4 sentences): Bridge crux to main message with data/examples
- Call-to-Action (1 sentence): Actionable, connects to message
- [10 keywords, comma-separated]
- 15 hashtags (mix popular and niche)

TONE GUIDELINES:
- Direct and confident - No fluff or motivational speak
- Data-driven - Include specific numbers, costs, timeframes when possible
- Anti-corporate - Avoid business jargon
- Systematic - Present frameworks and processes
- Authentic - Personal insights over generic advice

CRITICAL: The caption MUST start by defining/explaining the crux element, NOT summarizing the main script topic.

Return ONLY the formatted Instagram caption."""

        # System prompt for YouTube title generation
        self.youtube_prompt = """You are an expert YouTube title writer. Generate a title following these EXACT specifications:

REQUIREMENTS:
- Maximum 55 characters INCLUDING hashtags
- Exactly 2 hashtags
- Hook-focused: Create curiosity or urgency
- Specific: Include numbers, tools, or outcomes when possible

PATTERNS:
- "I Built a ₹28L Business With AI in 30 Days #AI #Business"
- "Stop Criticizing - Try This Instead #Psychology #Relationships"
- "Your Career is a Self-Deprecating Meme #AI #Career"

Return ONLY the YouTube title (no explanation)."""

    def identify_crux(self, script: str) -> Dict[str, str]:
        """
        Use Claude API to identify the crux element from script
        
        Args:
            script: Raw video script content
            
        Returns:
            Dict with 'crux_concept' and 'crux_definition' keys
        """
        try:
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=300,
                messages=[
                    {
                        "role": "user", 
                        "content": f"{self.crux_prompt}\n\nSCRIPT TO ANALYZE:\n{script}"
                    }
                ]
            )
            
            result = json.loads(response.content[0].text)
            return result
            
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                "crux_concept": "Systematic Approach",
                "crux_definition": "A systematic approach breaks down complex challenges into manageable, actionable steps."
            }
        except Exception as e:
            raise Exception(f"Error identifying crux: {str(e)}")

    def generate_instagram_caption(self, script: str, crux_data: Dict[str, str]) -> str:
        """
        Generate Instagram caption using Claude API
        
        Args:
            script: Raw video script content
            crux_data: Dict containing crux_concept and crux_definition
            
        Returns:
            Formatted Instagram caption
        """
        try:
            prompt = f"""SCRIPT: {script}

CRUX ELEMENT: {crux_data['crux_concept']}
CRUX DEFINITION: {crux_data['crux_definition']}

{self.instagram_prompt}"""

            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=800,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text.strip()
            
        except Exception as e:
            raise Exception(f"Error generating Instagram caption: {str(e)}")

    def generate_youtube_title(self, script: str, crux_data: Dict[str, str]) -> str:
        """
        Generate YouTube title using Claude API
        
        Args:
            script: Raw video script content  
            crux_data: Dict containing crux_concept and crux_definition
            
        Returns:
            YouTube title under 55 characters with 2 hashtags
        """
        try:
            prompt = f"""SCRIPT: {script}

CRUX ELEMENT: {crux_data['crux_concept']}

{self.youtube_prompt}"""

            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=100,
                messages=[{"role": "user", "content": prompt}]
            )
            
            title = response.content[0].text.strip()
            
            # Ensure title is under 55 characters
            if len(title) > 55:
                # Find the hashtags and truncate base title
                hashtag_start = title.rfind('#')
                if hashtag_start != -1:
                    hashtags = title[hashtag_start:]
                    base_title = title[:hashtag_start].strip()
                    max_base_length = 55 - len(hashtags) - 1  # -1 for space
                    if len(base_title) > max_base_length:
                        base_title = base_title[:max_base_length-3] + "..."
                    title = base_title + " " + hashtags
                else:
                    title = title[:52] + "..."
            
            return title
            
        except Exception as e:
            raise Exception(f"Error generating YouTube title: {str(e)}")

    def generate_content(self, script: str) -> Dict[str, str]:
        """
        Main function to generate both Instagram caption and YouTube title
        
        Args:
            script: Raw transcript or script content
            
        Returns:
            Dict with 'instagram_caption' and 'youtube_title' keys
        """
        if not script or not script.strip():
            raise ValueError("Script cannot be empty")
        
        try:
            # Step 1: Identify crux using Claude API
            crux_data = self.identify_crux(script)
            
            # Step 2: Generate Instagram caption
            instagram_caption = self.generate_instagram_caption(script, crux_data)
            
            # Step 3: Generate YouTube title
            youtube_title = self.generate_youtube_title(script, crux_data)
            
            return {
                "instagram_caption": instagram_caption,
                "youtube_title": youtube_title
            }
            
        except Exception as e:
            raise Exception(f"Error generating content: {str(e)}")


# Example usage and testing
if __name__ == "__main__":
    # Set API key from environment
    import os
    if not os.getenv('ANTHROPIC_API_KEY'):
        raise ValueError("ANTHROPIC_API_KEY environment variable is required")
    
    # Your script
    script = """Unfollow. Unsubscribe & Stop chasing every girl you'd settle for just to satisfy biological urges. You're not where you want to be, so cut the women - they are distractions.

If you painted out your dream dream dream girl not who you'd settle for but the mother of your children - you probably can't attract her right now.

So what's the point of wasting time in DMs, Tinder or getting drunk… just to settle for a woman who's subpar to the vision of who you'd wanna be with.

Lock yourself in your house. Work on yourself  and Present yourself to the world in 5 years and you'll get her like this."""
    
    try:
        generator = CaptionGenerator()
        print("✅ Successfully initialized CaptionGenerator")
        print("\n" + "="*60)
        print("TESTING YOUR SCRIPT")
        print("="*60)
        
        print(f"Script: {script[:100]}...")
        print()
        
        # Generate content
        result = generator.generate_content(script)
        
        print("✅ INSTAGRAM CAPTION:")
        print(result["instagram_caption"])
        print()
        
        print("✅ YOUTUBE TITLE:")
        print(f"'{result['youtube_title']}'")
        print(f"Length: {len(result['youtube_title'])} characters")
        
        # Validation
        if len(result['youtube_title']) <= 55:
            print("✅ Title length is within limit")
        else:
            print("❌ Title exceeds 55 character limit")
        
        hashtag_count = result['youtube_title'].count('#')
        if hashtag_count == 2:
            print("✅ Title has exactly 2 hashtags")
        else:
            print(f"❌ Title has {hashtag_count} hashtags (should be 2)")
        
        print("\n✅ Generation completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")