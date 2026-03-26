memory = []

def add_memory(user, bot):
    memory.append({"user": user, "bot": bot})

def get_memory():
    return memory[-5:]  # last 5 messages only