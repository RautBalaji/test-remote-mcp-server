import random
from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("simple-tools-server")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: The first number
        b: The second number
    """
    return a + b


@mcp.tool()
def roll_dice(sides: int = 6, count: int = 1) -> str:
    """Roll one or more dice.

    Args:
        sides: Number of sides on the die (default 6)
        count: Number of dice to roll (default 1)
    """
    rolls = [random.randint(1, sides) for _ in range(count)]
    return f"Rolls: {rolls} | Total: {sum(rolls)}"


if __name__ == "__main__":
    # Use "streamable-http" (or "sse") transport for remote deployment,
    # instead of the default "stdio" transport used for local dev.
    mcp.run(transport="http", host="0.0.0.0", port=8000)