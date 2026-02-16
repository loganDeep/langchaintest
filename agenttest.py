# chatollama_agent.py

from langchain_community.chat_models import ChatOllama
from langchain_core.tools import tool

# ---------------------------
# 1️⃣ Define tools
# ---------------------------

@tool(description="Say hello to a person by name")
def say_hello(name: str) -> str:
    return f"Hello, {name}! 👋"

@tool(description="Add two numbers, input as a,b")
def add_numbers(input: str) -> str:
    try:
        a, b = map(int, input.split(","))
        return f"The sum of {a} and {b} is {a+b}"
    except:
        return "Invalid input. Use format: a,b"

tools = {
    "say_hello": say_hello,
    "add_numbers": add_numbers
}

# ---------------------------
# 2️⃣ Initialize ChatOllama
# ---------------------------

llm = ChatOllama(
    model="phi3",
    temperature=0
)

# ---------------------------
# 3️⃣ Manual agent loop
# ---------------------------

def run_agent(user_input: str):
    prompt = f"""
You are a helpful assistant.

If the user wants to call a tool, respond ONLY in this format:
CALL_TOOL:<tool_name>:<tool_input>

Available tools: say_hello, add_numbers

User input: {user_input}
"""
    response = llm.invoke(prompt).content.strip()

    if response.startswith("CALL_TOOL:"):
        try:
            _, tool_name, tool_input = response.split(":", 2)
            tool_fn = tools.get(tool_name.strip())
            if not tool_fn:
                return f"Unknown tool: {tool_name}"
            return tool_fn(tool_input.strip())
        except Exception as e:
            return f"Error parsing tool call: {e}"

    return response

# ---------------------------
# 4️⃣ Run agent
# ---------------------------

if __name__ == "__main__":
    print(run_agent("Say hello to Deepu"))
    print(run_agent("Add 5,7"))
