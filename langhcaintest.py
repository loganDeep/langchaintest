
from langchain_community.chat_models import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
from fileLoader import loadFile 
from helper.llmmethods import InvokeLLM, getCurrentLLM, Timer
from fpdf import FPDF
def edit_cv_text(text: str) -> str:
    """If the text looks like a CV, add 'name : deepu' at the top."""
    # Simple heuristic: look for 'cv' or 'Curriculum Vitae' or 'Resume' in the text
    lower_text = text.lower()
    if 'cv' in lower_text or 'curriculum vitae' in lower_text or 'resume' in lower_text:
        return 'name : deepu\n' + text + '\n[Edited on 2026-02-17]'
    else:
        return text

def save_text_as_pdf(text: str, output_path: str):
    """Save the given text as a new PDF file using built-in font."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    # Replace unsupported characters with '?'
    safe_text = text.encode("latin-1", "replace").decode("latin-1")
    for line in safe_text.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.output(output_path)

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
    
    # Hard coded question
    question = """Respond with the edited cv  
    1.Change the name to Deepu Manoharan, do not change anything else.

    """

    print(f"Question: {question}\n")
    print("Processing...\n")
    
    # Timing the LLM invocation
    timer = Timer()
    timer.start()
    # Ask question using context
    response = InvokeLLM(llm, chunks, question)
    
        # Save the LLM response as a new PDF
    output_pdf = "filestore/edited_cv_output.pdf"
    save_text_as_pdf(response.content, output_pdf)
    print(f"✓ Saved edited CV as PDF: {output_pdf}\n")
    elapsed_time = timer.end()
    print(f"LLM processing took: {elapsed_time:.2f} seconds\n")
    print("Answer:")
    print("-" * 60)
    print(response.content)
    print("-" * 60)

if __name__ == "__main__":
    main()
