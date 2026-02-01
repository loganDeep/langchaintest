from langchain_community.chat_models import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

from helper.llmmethods import InvokeLLM, getCurrentLLM

def load_text_from_file(file_path: str) -> str:
    """Load text content from a file"""
    try:
        path = Path(file_path).expanduser().resolve()
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if not path.is_file():
            raise IsADirectoryError(f"Not a file: {file_path}")
        
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
        
    except Exception as e:
        print(f"Error loading file: {e}")
        return ""

def main():
    print("=" * 60)
    print("LangChain Q&A System")
    print("=" * 60)
    
    # Load text from file
    file_path = "data.txt"
    text = load_text_from_file(file_path)
    
    if not text:
        print(f"Could not load '{file_path}'. Please check the file exists.")
        return
    
    print(f"✓ Loaded '{file_path}' ({len(text)} characters)\n")

    # Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )
    chunks = splitter.split_text(text)
    print(f"✓ Created {len(chunks)} text chunks\n")

    # Local LLM (phi3)
    llm = getCurrentLLM()
    
    # Hard coded question
    question = "Who is REV9 and what is her expertise?"
    
    print(f"Question: {question}\n")
    print("Processing...\n")
    
    # Ask question using context
    response = InvokeLLM(llm, chunks, question)

    print("Answer:")
    print("-" * 60)
    print(response.content)
    print("-" * 60)

if __name__ == "__main__":
    main()
