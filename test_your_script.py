#!/usr/bin/env python3
"""
Test script for your specific content
"""

import os
from caption_generator import CaptionGenerator

def test_your_script():
    """Test with your specific script"""
    
    # Set API key from environment
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

if __name__ == "__main__":
    test_your_script()