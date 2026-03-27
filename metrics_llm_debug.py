# metrics_llm_debug.py
# Standalone script to load log file, send to LLM, and print payment error count
from helper.llmmethods import InvokeLLM, getCurrentLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter

def loadFile(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def main():
    file_path = "filestore/log.json"
    text = loadFile(file_path)
    payment_error_count = 0
    error_message = ""
    if not text:
        error_message = f"Could not load '{file_path}'"
    else:
        splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
        chunks = splitter.split_text(text)
        llm = getCurrentLLM()
        hardcoded_prompt = "Return only payment errors count as a number. Return only the number."
        try:
            response = InvokeLLM(llm, chunks, hardcoded_prompt)
            result = response.content if hasattr(response, "content") else str(response)
            import re
            match = re.search(r"(\d+)", result)
            payment_error_count = int(match.group(1)) if match else 0
        except Exception as e:
            error_message = str(e)
    print(f"payment_errors_count: {payment_error_count}")
    if error_message:
        print(f"error: {error_message}")

if __name__ == "__main__":
    main()
