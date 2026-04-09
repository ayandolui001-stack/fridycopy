import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# আপনার কাস্টম মডিউলগুলো
try:
    from ai import chat_ai
    from memory import add_memory
    from commands import run_command
except ImportError as e:
    print(f"Import Error: {e}. নিশ্চিত করুন ai.py, memory.py এবং commands.py ফাইলগুলো আছে।")

app = FastAPI()

# CORS সেটিংস (যদি ব্রাউজার থেকে রিকোয়েস্ট ব্লক হয় তবে এটি সাহায্য করবে)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# বর্তমান ডিরেক্টরি পাথ সেট করা
current_dir = os.path.dirname(os.path.realpath(__file__))

@app.post("/chat")
async def chat(message: str):
    # কমান্ড রান করার চেষ্টা
    cmd = run_command(message)
    if cmd:
        return {"response": cmd}

    # AI এর মাধ্যমে উত্তর তৈরি
    response = chat_ai(message)
    
    # মেমরিতে সেভ করা
    add_memory(message, response)

    return {"response": response}

# 👉 HTML UI মাউন্ট করা (সবার শেষে রাখা ভালো)
# আপনার ফাইলগুলো যেহেতু সরাসরি রুটেই আছে, তাই directory="." দেওয়া হয়েছে
app.mount("/", StaticFiles(directory=current_dir, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    
