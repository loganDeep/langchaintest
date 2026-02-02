from langchain_community.document_loaders import PyPDFLoader, TextLoader
from pathlib import Path

def loadFile(filePath: str) -> str:
    """
    Load content from a file based on its extension.
    Supports .pdf and .txt files.
    """
    try:
        text = ""
        path = Path(filePath).expanduser().resolve()
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filePath}")
        if not path.is_file():
            raise IsADirectoryError(f"Not a file: {filePath}")
        
        # Get file extension
        file_extension = path.suffix.lower()
        
        if file_extension == '.pdf':
            # Load PDF file
            loader = PyPDFLoader(str(path))
            documents = loader.load()
            text = "\n".join(doc.page_content for doc in documents)
        
        elif file_extension == '.txt':
            # Load text file using langchain TextLoader
            loader = TextLoader(str(path), encoding='utf-8')
            documents = loader.load()
            text = "\n".join(doc.page_content for doc in documents)
        
        else:
            raise ValueError(f"Unsupported file format: {file_extension}. Supported formats: .pdf, .txt")
        
        return text
    
    except Exception as e:
        print(f"Error loading file: {e}")
        return ""


def loadPythonPdf(pdfPath: str) -> str:
    """
    Legacy function - loads PDF files.
    Use loadFile() for more flexible file handling.
    """
    try:
        text = ""
        path = Path(pdfPath).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"File not found: {pdfPath}")
        if not path.is_file():
            raise IsADirectoryError(f"Not a file: {pdfPath}") 

        loader = PyPDFLoader(str(path))
        documents = loader.load()   
       
        text = "\n".join(doc.page_content for doc in documents)    
        return text
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return ""