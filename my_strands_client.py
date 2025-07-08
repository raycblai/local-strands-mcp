from mcp.client.streamable_http import streamablehttp_client
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient

def create_streamable_http_transport():
    return streamablehttp_client("http://localhost:8000/mcp/")  # Adjust port/path as needed

streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

with streamable_http_mcp_client:
    tools = streamable_http_mcp_client.list_tools_sync()
    agent = Agent(tools=tools)
    
    # Example 1: Addition
    print("Example 1: Addition")
    print(agent("Add 2 and 3"))
    
    # Example 2: Sorting
    print("\nExample 2: Sorting")
    print(agent("Sort these numbers: 5, 2, 9, 1, 7, 3"))
