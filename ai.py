from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_ai(message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are JARVIS, a smart AI assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content