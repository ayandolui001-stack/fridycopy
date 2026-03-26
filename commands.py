def run_command(text):
    text = text.lower()

    if "time" in text:
        from datetime import datetime
        return f"Current time is {datetime.now().strftime('%H:%M')}"

    if "your name" in text:
        return "I am JARVIS, your assistant."

    return None