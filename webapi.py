# Random metrics endpoint for testing
import random

from fastapi.responses import PlainTextResponse
 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from fileLoader import loadFile
from helper.llmmethods import InvokeLLM, getCurrentLLM

app = FastAPI()



@app.get("/metrics-prometheus", response_class=PlainTextResponse)
async def metrics_random():
    value = random.randint(0, 49)
    return f"payment_errors_count {value}\n"


class AskRequest(BaseModel):
    prompt: str


# Prometheus metrics endpoint
from fastapi.responses import PlainTextResponse


@app.get("/metrics-prometheusdown", response_class=PlainTextResponse)
async def metrics_prometheus():
    file_path = "filestore/log.json"
    text = loadFile(file_path)
    if not text:
        return ""  # Prometheus expects 200 with empty body if no data
    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split_text(text)
    llm = getCurrentLLM()
    hardcoded_prompt = "Return only payment errors count as a number. Return only the number."
    response = InvokeLLM(llm, chunks, hardcoded_prompt)
    result = response.content if hasattr(response, "content") else str(response)
    # Prometheus expects plain text, e.g., metric_name value\n
    # Try to extract a number from the LLM result for Prometheus format
    import re
    match = re.search(r"(\d+)", result)
    if match:
        return f"payment_errors_count {match.group(1)}\n"
    else:
        return f"payment_errors_count 0\n"  # fallback if LLM doesn't return a number
 
 
@app.get("/metrics")
async def metrics():
    file_path = "filestore/log.json"
    text = loadFile(file_path)
    if not text:
        raise HTTPException(status_code=404, detail=f"Could not load '{file_path}'")
    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split_text(text)
    llm = getCurrentLLM()
    hardcoded_prompt = "Return only payment errors count as a number. Return only the number."
    response = InvokeLLM(llm, chunks, hardcoded_prompt)
    result = response.content if hasattr(response, "content") else str(response)
    return {"llm_response": result}


@app.get("/ask")
async def ask_endpoint():
    file_path = "filestore/log.json"
    text = loadFile(file_path)
    if not text:
        raise HTTPException(status_code=404, detail=f"Could not load '{file_path}'")
    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split_text(text)
    llm = getCurrentLLM()
    hardcoded_prompt = "Return only payment errors count as a number. Return only the number."
    response = InvokeLLM(llm, chunks, hardcoded_prompt)
    result = response.content if hasattr(response, "content") else str(response)
    return {"llm_response": result}
