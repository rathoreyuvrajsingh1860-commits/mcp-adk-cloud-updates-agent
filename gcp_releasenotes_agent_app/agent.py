from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioServerParameters

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="AI agent that can fetch Google Cloud release notes",
    instruction="Answer user questions using available tools when needed.",
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="/home/ladusingh505/mcp-toolbox/toolbox",
                args=[
                    "--tools-file",
                    "/home/ladusingh505/mcp-toolbox/tools.yaml",
                    "--stdio"
                ]
            )
        )
    ]
)