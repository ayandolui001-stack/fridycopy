import edge_tts
import asyncio

async def speak(text):
    communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
    await communicate.save("output.mp3")