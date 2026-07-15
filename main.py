import asyncio
from mcp.server.fastmcp import FastMCP

# FastMCP 서버 인스턴스 생성
mcp = FastMCP("ArithmeticCalculator")

# 1. 덧셈 도구
@mcp.tool()
def add(a: float, b: float) -> float:
    """두 숫자를 더합니다."""
    return a + b

# 2. 뺄셈 도구
@mcp.tool()
def subtract(a: float, b: float) -> float:
    """첫 번째 숫자에서 두 번째 숫자를 뺍니다."""
    return a - b

# 3. 곱셈 도구
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """두 숫자를 곱합니다."""
    return a * b

# 4. 나눗셈 도구
@mcp.tool()
def divide(a: float, b: float) -> float:
    """첫 번째 숫자를 두 번째 숫자로 나눕니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

if __name__ == "__main__":
    # Stdio 방식으로 서버 실행
    mcp.run()
