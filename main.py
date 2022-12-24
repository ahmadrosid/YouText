from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from transcribe import transcribe

app = FastAPI()

@app.get("/")
def index():
    index = ""
    with open("static/index.html", "r") as f:
        index = f.read()
    return HTMLResponse(index)

@app.post("/api")
def api(url: str = Form()):
    data = transcribe(url)
    return {
        "url": url,
        "data": data
    }
