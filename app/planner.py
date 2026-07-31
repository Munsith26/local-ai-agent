from app.llm import chat_with_ai


def choose_tool(user_message: str):
    prompt = f"""
You are an AI agent.

Available tools:

1. calculator
   Use for mathematical calculations.

2. time
   Use when the user asks for the current time.

3. rag
   Use when the user asks about uploaded PDFs or documents.

4. chat
   Use for normal conversation.

Return ONLY ONE WORD.

calculator
time
rag
chat

User:
{user_message}
"""

    decision = chat_with_ai(prompt)

    return decision.strip().lower()