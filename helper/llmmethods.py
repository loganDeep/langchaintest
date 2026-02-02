from langchain_community.chat_models import ChatOllama
import time

class Timer:
    """Reusable timer class to measure execution time"""
    
    def __init__(self):
        self.start_time = None
        self.end_time = None
    
    def start(self) -> None:
        """Start the timer"""
        self.start_time = time.time()
    
    def end(self) -> float:
        """End the timer and return elapsed time in seconds"""
        self.end_time = time.time()
        if self.start_time is None:
            raise ValueError("Timer was not started. Call start() first.")
        elapsed_time = self.end_time - self.start_time
        return elapsed_time
    
    def get_formatted_time(self) -> str:
        """Return formatted elapsed time as a readable string"""
        if self.start_time is None:
            raise ValueError("Timer was not started. Call start() first.")
        elapsed_time = self.end()
        
        if elapsed_time < 1:
            return f"{elapsed_time * 1000:.2f}ms"
        elif elapsed_time < 60:
            return f"{elapsed_time:.2f}s"
        else:
            minutes = elapsed_time // 60
            seconds = elapsed_time % 60
            return f"{int(minutes)}m {seconds:.2f}s"


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

