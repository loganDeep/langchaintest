
from langchain_community.chat_models import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
from fileLoader import loadFile 
from helper.llmmethods import InvokeLLM, getCurrentLLM, Timer


def main():
    print("=" * 60)
    print("LangChain Q&A System")
    print("=" * 60)
    
    # Load text from file (PDF or TXT)
    file_path = "filestore/log.json"  # Use the CV PDF file
    text = loadFile(file_path)
    
    if not text:
        print(f"Could not load '{file_path}'. Please check if the file exists.")
        return
    
    print(f"✓ Loaded '{file_path}' ({len(text)} characters)\n")

    # --- Continue with chunking and LLM as before ---
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )
    chunks = splitter.split_text(text)
    print(f"✓ Created {len(chunks)} text chunks\n")

    # Local LLM (phi3)
    llm = getCurrentLLM()
    
    import json
    import time
    from datetime import datetime
    # user_q = input("You: ")  # Commented as per instructions
    prompt = (
        "Return only payment errors in valid JSON array format. No quotes at the start, no explanation, just a JSON array, nothing else."
    )
    print("Starting error polling loop. Press Ctrl+C to stop.")
    try:
        while True:
            print("Polling for errors...")
            timer = Timer()
            timer.start()
            response = InvokeLLM(llm, chunks, prompt)
            elapsed_time = timer.end()
            print(f"LLM processing took: {elapsed_time:.2f} seconds\n")
            print("Result:")
            print("-" * 60)
            print(response.content)
            print("-" * 60)
            # Write only the raw response content (JSON array) to filestore/processed.log
            with open("filestore/processed.log", "a", encoding="utf-8") as f:
                f.write(response.content.strip() + "\n")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nExiting.")
    except Exception as e:
        print(f"Error: {e}")
            

if __name__ == "__main__":
    main()
