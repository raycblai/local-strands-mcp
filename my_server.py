from mcp.server.fastmcp import FastMCP
import datetime
import uvicorn

mcp = FastMCP("My Custom Server")

@mcp.tool(description="Add two numbers together")
def add(x: int, y: int) -> int:
    return x + y

mcp.run(transport="streamable-http")  # Or "stdio" for standard I/O
