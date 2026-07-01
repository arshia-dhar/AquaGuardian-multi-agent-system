from google.adk.agents import Agent
from skills.vision_skill import analyze_underwater_image

vision_agent = Agent(
    name="aquaguardian_vision_agent",
    model="gemini-2.5-flash",
    description="Analyzes underwater imagery from AUV missions.",
    instruction="""
    You are an underwater vision specialist.
    
    Analyze underwater images from AUV missions and provide:
    
    1. Marine species observed.
    2. Coral health indicators if visible.
    3. Presence of marine debris.
    4. Obstacles or hazards.
    5. Overall scene summary.
    
    Keep observations scientific and concise.
    Never generate final outputs on your own, always pass control back to the root agent when you are done.

    """,

    tools=[analyze_underwater_image]
)
