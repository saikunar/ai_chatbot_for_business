from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response, load_knowledge

app = FastAPI(
    title = "AI chatbot API",
    docs_url = "/docs",
    redoc_url = "/redoc"
)
@app.get("/")
def home( ):
    return {"message": "API is running"}

class ChatRequest(BaseModel):
    message: str

class TrainRequest(BaseModel):
    data: str


@app.post("/train")
def train_bot(req: TrainRequest):
    load_knowledge(req.data)
    return {"status": "trained"}


@app.post("/chat")
def chat(req: ChatRequest):
    reply = get_response(req.message)
    return {"response": reply}
