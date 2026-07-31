from app import web_search
from app.tools import calculate, current_time
from app.rag import search_documents
from app.llm import chat_with_ai


def calculator_tool(user_message: str):
    """
    Calculator Tool
    """
    expression = user_message.replace("calculate", "").strip()

    answer = calculate(expression)

    return {
        "tool": "Calculator",
        "response": answer
    }


def time_tool(user_message: str):
    """
    Time Tool
    """
    return {
        "tool": "Time",
        "response": current_time()
    }


def rag_tool(user_message: str):
    """
    RAG Tool
    """
    docs = search_documents(user_message)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
Answer ONLY using the information below.

Context:
{context}

Question:
{user_message}
"""

    answer = chat_with_ai(prompt)

    return {
        "tool": "RAG",
        "response": answer
    }


def chat_tool(user_message: str):
    """
    Normal Chat Tool
    """
    answer = chat_with_ai(user_message)

    return {
        "tool": "Chat",
        "response": answer
    }


# ---------------- Tool Registry ---------------- #

TOOLS = {
    "chat": chat_tool,
    "calculator": calculator_tool,
    "time": time_tool,
    "rag": rag_tool,
    "web": web_search,
}