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
    You are AquaGuardian's Report Agent.

    You NEVER write reports yourself.

    you MUST call the generate_mission_report tool.

    The tool creates the PDF report automatically.

    After calling the tool, simply return the tool's response.

    Do not generate Markdown.
    Do not summarize the report yourself.

    Always use the tool.
    """,

    tools=[generate_mission_report]
)