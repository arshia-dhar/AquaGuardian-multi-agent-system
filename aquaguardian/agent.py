from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StdioConnectionParams
)
from mcp import StdioServerParameters

from .agents.vision_agent import vision_agent
from .agents.telemetry_agent import telemetry_agent
from .agents.research_agent import research_agent
from .agents.report_agent import report_agent

from security.prompt_guard import guard_user_request

root_agent = Agent(
    name="aquaguardian",
    model="gemini-2.5-flash",
    description="Coordinates underwater mission analysis.",
    instruction="""
    Before processing any user request, always call
    guard_user_request on the user's message.

    If the request is flagged as malicious, refuse to continue.

    Otherwise continue normally:

    You are AquaGuardian, an autonomous underwater mission analyst.

    For complete mission analysis you MUST follow this exact sequence:

    1. Use get_latest_mission.
    2. Use get_mission_files.
    3. Transfer to telemetry_agent for CSV analysis.
    4. After telemetry analysis returns, transfer to vision_agent for image analysis.
    5. After vision analysis returns, transfer to research_agent for ecological interpretation. 
    (The Report Agent requires the Research Agent's output. A report is incomplete without ecological interpretation.)  
    6. Finally transfer to report_agent to generate the final report.

    Never stop after a single agent completes.
    Continue until ALL four agents have participated.

    A complete mission analysis ALWAYS requires:
    - telemetry_agent
    - vision_agent
    - research_agent
    - report_agent
    """,

    tools=[
        guard_user_request,

        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="python",
                    args=["mcp_servers/filesystem_server.py"]
                )
            )
        )
    ],

    sub_agents=[
        vision_agent,
        telemetry_agent,
        research_agent,
        report_agent
    ]
)