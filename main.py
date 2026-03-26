from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()

app = FastAPI()

# Initialize LLM (lightweight, API based)
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# Request model
class ChatRequest(BaseModel):
    message: str

# Home route
@app.get("/")
def home():
    return {"status": "FRIDAY is running 🚀"}

# Chat route
@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        response = llm.invoke(req.message)
        return {
            "reply": response.content
        }
    except Exception as e:
        return {"error": str(e)}