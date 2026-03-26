from fastapi import FastAPI
from ai import chat_ai
from memory import add_memory
from commands import run_command

app = FastAPI()

@app.get("/")
def home():
    return {"message": "JARVIS is online 🚀"}

@app.post("/chat")
def chat(message: str):
    cmd = run_command(message)

    if cmd:
        return {"response": cmd}

    response = chat_ai(message)
    add_memory(message, response)

    return {"response": response}
