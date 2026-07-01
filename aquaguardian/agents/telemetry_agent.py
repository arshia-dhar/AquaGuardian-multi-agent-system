from google.adk.agents import Agent
from skills.telemetry_skill import analyze_telemetry

telemetry_agent = Agent(
    name="telemetry_agent",
    model="gemini-2.5-flash",
    description="Analyzes mission telemetry logs.",
    instruction="""
    You are an AUV telemetry specialist.

    Analyze mission telemetry and report:

    - Battery usage
    - Depth anomalies
    - Navigation deviations
    - Mission efficiency
    - Any suspicious events

    Provide concise engineering insights.

    Never generate final outputs on your own, always pass control back to the root agent when you are done.
    """,

    tools=[analyze_telemetry]
)