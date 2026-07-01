from google.adk.agents import Agent
from skills.report_skill import (
    generate_mission_report
)

report_agent = Agent(
    name="report_agent",
    model="gemini-2.5-flash",

    description="""
    Generates comprehensive mission reports.
    """,

    instruction="""
    Use the generate_mission_report tool to
    create detailed PDF mission reports.

    Always include:
    - Vision findings
    - Telemetry findings
    - Scientific insights
    - Recommendations
    """,

    tools=[generate_mission_report]
)