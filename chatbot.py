import requests
import json

context_data = ""

def load_knowledge(text):
    global context_data
    context_data = text


def get_response(user_input):
    prompt = f"""
You are a professional business chatbot.

Business Info:
{context_data}

User Question:
{user_input}

Answer clearly and professionally:
"""

    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt
        },
        stream=True
    )

    full_response = ""

    for line in res.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            full_response += data.get("response", "")

    return full_response