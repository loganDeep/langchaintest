from langchain_community.chat_models import ChatOllama

#make this better later by adding more LLM options
def getCurrentLLM():
    """Get current LLM instance (ChatOllama with phi3 model)"""
    llm = ChatOllama(model="phi3")
    return llm

def InvokeLLM(llm, context, question: str):
    """Invoke the LLM with the given context and question, return the response"""
    # Handle both list of chunks and string context
    if isinstance(context, list):
        context_str = "\n".join(context)
    else:
        context_str = context
    
    prompt = f"Use ONLY this context:\n{context_str}\n\nQuestion: {question}"
    response = llm.invoke(prompt)
    return response

