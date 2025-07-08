from mcp.server.fastmcp import FastMCP
import datetime
import uvicorn
from typing import List

mcp = FastMCP("My Custom Server")

@mcp.tool(description="Add two numbers together")
def add(x: int, y: int) -> int:
    return x + y

@mcp.tool(description="Sort a list of numbers in descending order")
def descending_sorting(numbers: List[float]) -> List[float]:
    """
    Sort a list of numbers in descending order.
    
    Args:
        numbers: A list of numbers to sort
        
    Returns:
        A new list with the numbers sorted in descending order
    """
    return sorted(numbers, reverse=True)

@mcp.tool(description="Sort a list of numbers in ascending order")
def ascending_sorting(numbers: List[float]) -> List[float]:
    """
    Sort a list of numbers in ascending order.
    
    Args:
        numbers: A list of numbers to sort
        
    Returns:
        A new list with the numbers sorted in ascending order
    """
    return sorted(numbers)

mcp.run(transport="streamable-http")  # Or "stdio" for standard I/O
