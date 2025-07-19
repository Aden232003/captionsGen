#!/usr/bin/env python3
"""
Test script for Caption Generator
Run this to test the generator with example scripts
"""

import os
from caption_generator import CaptionGenerator

def test_generator():
    """Test the caption generator with provided examples"""
    
    # Check if API key is set
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("❌ Error: ANTHROPIC_API_KEY environment variable is not set")
        print("\nTo set it:")
        print("export ANTHROPIC_API_KEY='your-api-key-here'")
        return
    
    try:
        generator = CaptionGenerator()
        print("✅ Successfully initialized CaptionGenerator")
        
        # Test scripts from the specification
        test_scripts = [
            {
                "name": "AI Business Script",
                "script": "I just built an entire business using AI in one month. What used to take me 3 months and cost 50,000 rupees now costs 10-12,000 rupees. I scraped 2000 qualified emails using Apollo and Cursor AI built my automation scripts. My offer ranges from $5,000 to $28,000 per month per client. While people debate AI taking jobs, I'm using it to build businesses.",
                "expected_crux": "Should identify Apollo, Cursor AI, or Web scraping"
            },
            {
                "name": "Psychology/Relationships Script", 
                "script": "You'll never have successful relationships until you stop criticizing. Most people think criticism changes behavior. It doesn't. Dale Carnegie School has audiences only compliment speakers, never criticize. Result? Confident students develop faster. I used to point out what's wrong. Now I amplify what's right.",
                "expected_crux": "Should identify Dale Carnegie School method"
            },
            {
                "name": "Content Consumption Script",
                "script": "You can't live a big life consuming small minds. Stay watching wrong content and you shrink. If everyone you watch makes memes, posts random content, or stays too relaxed, you won't push yourself either. The second you consume bigger minds, everything changes.",
                "expected_crux": "Should identify Algorithm or Content curation"
            }
        ]
        
        print("\n" + "="*60)
        print("TESTING CAPTION GENERATOR")
        print("="*60)
        
        for i, test_case in enumerate(test_scripts, 1):
            print(f"\n--- Test {i}: {test_case['name']} ---")
            print(f"Expected Crux: {test_case['expected_crux']}")
            print(f"Script: {test_case['script'][:100]}...")
            print()
            
            try:
                # Generate content
                result = generator.generate_content(test_case['script'])
                
                print("✅ INSTAGRAM CAPTION:")
                print(result["instagram_caption"])
                print()
                
                print("✅ YOUTUBE TITLE:")
                print(f"'{result['youtube_title']}'")
                print(f"Length: {len(result['youtube_title'])} characters")
                
                # Check if title is under 55 characters
                if len(result['youtube_title']) <= 55:
                    print("✅ Title length is within limit")
                else:
                    print("❌ Title exceeds 55 character limit")
                
                # Check if title has exactly 2 hashtags
                hashtag_count = result['youtube_title'].count('#')
                if hashtag_count == 2:
                    print("✅ Title has exactly 2 hashtags")
                else:
                    print(f"❌ Title has {hashtag_count} hashtags (should be 2)")
                
                print("\n" + "-"*50)
                
            except Exception as e:
                print(f"❌ Error processing test {i}: {str(e)}")
                print("-"*50)
        
        print("\n✅ Testing completed!")
        
    except Exception as e:
        print(f"❌ Error initializing generator: {str(e)}")

if __name__ == "__main__":
    test_generator()