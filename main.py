from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from ai import chat_ai
from memory import add_memory
from commands import run_command

app = FastAPI()

# 👉 This will show your HTML UI
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


@app.post("/chat")
def chat(message: str):
    cmd = run_command(message)

    if cmd:
        return {"response": cmd}

    response = chat_ai(message)
    add_memory(message, response)

    return {"response": response}
