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
    print("\nExample 2: Down Sorting")
    print(agent("Sort these numbers in descending order: 5, 2, 9, 1, 7, 3"))

    # Example 3: Sorting
    print("\nExample 3: Up Sorting")
    print(agent("Sort these numbers in ascending order: 5, 2, 109, 1, -7, -30"))
    
    # Example 4: Tool selection test
    print("\nExample 4: Tool selection test")
    print(agent("What is 10 plus 15?"))
    
    # Example 5: Another tool selection test
    print("\nExample 5: Another tool selection test")
    print(agent("Can you put these values in order: 42, 17, 33, 8, 21?"))
