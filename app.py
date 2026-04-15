from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response, load_knowledge

app = FastAPI(
    title = "AI chatbot API",
    d0cs_url = "/docs",
    redoc_url = "/redoc"
)

class ChatRequest(BaseModel):
    message: str

class TrainRequest(BaseModel):
    data: str


@app.post("/train")
def train_bot(req: TrainRequest):
    try:
        load_knowledge(req.data)
        return {"status": "trained"}
    except Exception as e:
        return {"status": f"error: {str(e)}"}


@app.post("/chat")
def chat(req: ChatRequest):
    try:
        response = get_response(req.message)
        return {"response": response}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}
