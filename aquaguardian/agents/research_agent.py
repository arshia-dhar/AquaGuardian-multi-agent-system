from google.adk.agents import Agent
from skills.research_skill import get_ecological_insights

research_agent = Agent(
    name="research_agent",
    model="gemini-2.5-flash",
    description="Provides scientific context for underwater observations.",
    instruction="""
    You are a marine science research assistant.

    Given detected species or observations,
    provide relevant scientific background,
    ecological importance, and conservation insights.

    Keep responses factual and concise.
    Never generate final outputs on your own, always pass control back to the root agent when you are done.

    """,

    tools=[get_ecological_insights]
)