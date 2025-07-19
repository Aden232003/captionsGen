Instagram Caption & YouTube Title Generator Prompt
Project Overview
Create a Python 3 application that generates Instagram captions and YouTube titles from video script inputs, following specific formatting and content guidelines.

Core Requirements
Input Format
Script Text: Raw transcript or script content from short-form videos (30-90 seconds)
Content Type: Reel/Short-form video content focused on business, AI, personal development, philosophy
Output Format
Instagram Caption (150-300 words + hashtags + keywords)
YouTube Title (Under 55 characters including hashtags)
Instagram Caption Structure
Format Requirements:
Hook Paragraph (2-3 sentences)
Identify a specific tool, concept, or "crux" from the script (see Crux Definition below)
Define/explain this element concisely
Don't just summarize the main topic
Connection Paragraph (3-4 sentences)
Bridge the crux concept to the main script message
Include supporting data, examples, or consequences
Maintain authoritative, direct tone
Call-to-Action Line (1 sentence)
Actionable, non-generic
Connects to the overall message
Bracketed Keywords (10 keywords, comma-separated)
Relevant to both the crux concept and main message
Mix of broad and specific terms
Hashtags (15 hashtags)
Mix of popular and niche tags
Relevant to content pillars
What is a "Crux" Element?
The crux is a specific, tangible element mentioned in the script that can be defined or explained, rather than the main overarching message.

Crux Examples:
Example 1:

Script Main Topic: "AI is changing careers and making degrees obsolete"
Crux Element: "Claude Code" (a specific AI coding tool mentioned)
Caption Start: "Claude Code is an AI coding assistant that runs directly in your terminal..."
Example 2:

Script Main Topic: "Stop criticizing people if you want better relationships"
Crux Element: "Dale Carnegie School method" (specific technique mentioned)
Caption Start: "The Dale Carnegie School proved this by having audiences only compliment speakers, never criticize..."
Example 3:

Script Main Topic: "Your content consumption shapes your mindset"
Crux Element: "The algorithm" (specific mechanism mentioned)
Caption Start: "The algorithm is a mental diet that most people never consciously curate..."
How to Identify the Crux:
Look for specific tools, methods, or systems mentioned in the script
Find concrete examples or case studies referenced
Identify technical concepts or frameworks that can be defined
Choose something that can be explained independently but connects to the main message
Avoid the main theme itself - focus on supporting elements
If No Clear Crux Exists:
Create one from a specific aspect of the topic (e.g., "Web scraping at scale" from a broader AI business topic)
Focus on a particular technique or approach mentioned
Highlight a specific consequence or result that can be expanded upon
Tone Guidelines:
Direct and confident - No fluff or motivational speak
Data-driven - Include specific numbers, costs, timeframes
Anti-corporate - Avoid business jargon
Systematic - Present frameworks and processes
Authentic - Personal insights over generic advice
Content Strategy:
Value-First: Every sentence should provide actionable insight
Specificity: Use exact numbers, tools, timeframes
Bridge Building: Connect crux naturally to main message
Authority: Write from position of experience and knowledge
YouTube Title Structure
Format Requirements:
Maximum 55 characters including hashtags
2 hashtags maximum
Hook-focused: Create curiosity or urgency
Specific: Include numbers, tools, or outcomes when possible
Title Patterns:
"I Built a ₹28L Business With AI in 30 Days #AI #Business"
"Your Career is a Self-Deprecating Meme #AI #Career"
"Stop Criticizing - Try This Instead #Psychology #Relationships"
Content Pillars to Reference:
Expert-Level Trading Insights
AI-Driven Automation & Content Creation
Entrepreneurial Insights & Scaling
Philosophical Integration & Life Mastery
Systematic Outreach Strategies
Market Positioning Strategies
Men's Biology & Self-Mastery
Processing Logic:
Analyze script for main themes and supporting concepts
Identify crux element using definition above - specific tool, framework, or unique angle mentioned
Extract key data points - numbers, timeframes, costs, results
Determine content pillar alignment
Generate hook focusing on crux element definition/explanation
Build connection from crux to main message
Create CTA that matches content type
Select keywords and hashtags relevant to both crux and main theme
Technical Specifications:
Language: Python 3
Input: Text string (script content)
Output: Formatted dictionary with 'instagram_caption' and 'youtube_title' keys
Dependencies: Standard libraries preferred, external APIs if needed for enhanced processing
Error Handling: Graceful handling of various script lengths and formats
Follow-up Implementation Prompt
Please create a Python 3 application based on the specifications in the attached .md file that:

Takes a video script as input
Analyzes the content to identify the "crux" element (specific tool, concept, or unique angle mentioned - NOT the main theme)
Generates an Instagram caption starting with the crux definition, then bridging to main message
Creates a YouTube title under 55 characters with hashtags
Returns both in a formatted output
Input Examples with Expected Crux Identification:
Example 1 - AI Business Script:
I just built an entire business using AI in one month. What used to take me 3 months and cost 50,000 rupees now costs 10-12,000 rupees. I scraped 2000 qualified emails using Apollo and Cursor AI built my automation scripts. My offer ranges from $5,000 to $28,000 per month per client. While people debate AI taking jobs, I'm using it to build businesses.
Expected Crux: "Web scraping" or "Cursor AI" (specific tools mentioned) Caption Should Start: "Web scraping at scale used to require entire development teams..." OR "Cursor AI can build custom scripts that automate lead generation..."

Example 2 - Psychology/Relationships Script:
You'll never have successful relationships until you stop criticizing. Most people think criticism changes behavior. It doesn't. Dale Carnegie School has audiences only compliment speakers, never criticize. Result? Confident students develop faster. I used to point out what's wrong. Now I amplify what's right.
Expected Crux: "Dale Carnegie School method" (specific technique mentioned) Caption Should Start: "The Dale Carnegie School proved this by having audiences only compliment speakers, never criticize..."

Example 3 - Content Consumption Script:
You can't live a big life consuming small minds. Stay watching wrong content and you shrink. If everyone you watch makes memes, posts random content, or stays too relaxed, you won't push yourself either. The second you consume bigger minds, everything changes.
Expected Crux: "Algorithm" or "Content curation" (mechanism behind content consumption) Caption Should Start: "The algorithm is a mental diet that most people never consciously curate..." OR "Content curation is like nutrition for your mind..."

Expected Output Format:
python
{
    "instagram_caption": "Full formatted caption with crux definition start, bridge paragraph, CTA, [keywords], and #hashtags",
    "youtube_title": "Title Under 55 Chars #Tag #Tag"
}
Critical: The Instagram caption MUST start by defining/explaining the crux element, NOT by summarizing the main script topic. Then bridge from that crux to the main message.




