from langchain_core.tools import tool


@tool(description="Greet a person by name")
def say_hello(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}! Nice to meet you."
