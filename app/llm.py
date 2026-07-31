import ollama
from app.config import MODEL


SYSTEM_PROMPT = """
You are a helpful AI assistant.

Rules:
- Answer in clear, natural English.
- Keep responses concise (around 100-150 words) unless the user asks for more detail.
- Explain concepts simply.
- Use bullet points only when they improve readability.
- Do NOT use Markdown formatting like **, *, or #.
- If the user asks for code, return clean code with a short explanation.
- If the user asks a short question, give a short answer.
- If the user asks for a detailed explanation, provide one.
"""


def chat_with_ai(prompt: str, history=None):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    if history:
        for chat in history:
            messages.append(
                {
                    "role": "user",
                    "content": chat["user"]
                }
            )

            messages.append(
                {
                    "role": "assistant",
                    "content": chat["assistant"]
                }
            )

    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    response = ollama.chat(
        model=MODEL,
        messages=messages,
        options={
            "temperature": 0.3
        }
    )

    return response["message"]["content"]


def choose_tool(user_message: str):
    prompt = f"""
You are an AI tool selector.

Available tools:

calculator - Solve mathematical calculations.
time - Get the current date and time.
rag - Answer questions using indexed PDF documents.
web - Search the internet for current events, latest news, weather, websites, live information, recent technologies, and anything requiring up-to-date knowledge.
chat - General conversation.

Return ONLY ONE WORD from the list below.

calculator
time
rag
web
chat

User:
{user_message}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0
        }
    )

    return response["message"]["content"].strip().lower()