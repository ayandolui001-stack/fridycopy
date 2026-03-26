const API_URL = "https://fridycopy.onrender.com/chat";

function addMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");

  const msg = document.createElement("div");
  msg.classList.add("message", sender);
  msg.innerText = text;

  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const input = document.getElementById("message");
  const text = input.value;

  if (!text) return;

  addMessage(text, "user");
  input.value = "";

  const res = await fetch(`${API_URL}?message=${text}`, {
    method: "POST"
  });

  const data = await res.json();
  addMessage(data.response, "bot");
}