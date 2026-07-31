from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.agent import run_agent
from app.memory import conversation_memory

app = FastAPI(title="Local AI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    session_id: str
    message: str


@app.get("/")
def home():
    return {
        "message": "Local AI Agent is running!"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    return run_agent(
        request.session_id,
        request.message
    )


@app.get("/history/{session_id}")
def history(session_id: str):
    return conversation_memory.get(session_id, [])


@app.delete("/history/{session_id}")
def clear_history(session_id: str):
    conversation_memory.pop(session_id, None)

    return {
        "message": "Conversation history cleared."
    }