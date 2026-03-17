from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.chat_models import ChatOllama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from fileLoader import loadFile
from helper.llmmethods import InvokeLLM, getCurrentLLM

app = FastAPI()


class AskRequest(BaseModel):
    prompt: str


@app.post("/ask")
async def ask_endpoint(req: AskRequest):
    file_path = "filestore/log.json"
    text = loadFile(file_path)
    if not text:
        raise HTTPException(status_code=404, detail=f"Could not load '{file_path}'")

    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split_text(text)

    llm = getCurrentLLM()

    try:
        response = InvokeLLM(llm, chunks, req.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM call failed: {str(e)}")

    return {
        "query": req.prompt,
        "model": "phi3",
        "answer": response.content if hasattr(response, "content") else str(response),
        "status_code": getattr(response, "status_code", None),
    }
