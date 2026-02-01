from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
def loadPythonPdf(pdfPath:str)->str:
   

    try:
        text = ""
        path = Path(pdfPath).expanduser().resolve()
        if not path.exists():
            raise FileNotFoundError(f"File not found: {pdfPath}")
        if not path.is_file():
            raise IsADirectoryError(f"Not a file: {pdfPath}") 

        loader = PyPDFLoader(str(path))
        documents = loader.load()   
       
        text = "\n".join(doc.page_content  for doc in documents)    
        return text
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return ""