1.python 3.11.9 - To avoid issues with langchain
2.use model ollama phi3
Download and install https://ollama.com/download
and in Ollama UI select "phi3". This will download the right model
3.Additionally you can go to ~/helper/llmmethods.py and change this line
lm = ChatOllama(model="phi3") to select the model you want to use

4.Web API (FastAPI) instructions
- install: pip install fastapi uvicorn
- start: uvicorn webapi:app --reload --host 0.0.0.0 --port 8000

- sample request:
  curl -X POST "http://127.0.0.1:8000/ask" \
    -H "Content-Type: application/json" \
    -d '{"prompt":"Return only payment errors in JSON array format"}'

- response structure example:
  {
    "query": "Return only payment errors in JSON array format",
    "model": "llama3.1",
    "answer": "[ ... ]",
    "status_code": null
  }


