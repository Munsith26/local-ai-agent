from app.llm import chat_with_ai, choose_tool
from app.memory import get_history, add_to_history
from app.web_search import web_search

from app.tools import calculate, current_time
from app.rag import (
    list_documents,
    create_vector_db,
    search_documents,
)


def run_agent(session_id: str, user_message: str):

    history = get_history(session_id)

    message = user_message.lower()

    # ---------------- PDF Commands ----------------

    if message == "list pdfs":
        return {
            "tool": "PDF Manager",
            "response": list_documents()
        }

    if message == "index pdfs":
        return {
            "tool": "RAG",
            "response": create_vector_db()
        }

    # ---------------- AI Tool Selection ----------------

    tool = choose_tool(user_message)

    print(f"\nSelected Tool: {tool}\n")

    # ---------------- Calculator ----------------

    if tool == "calculator":

        expression = (
            user_message
            .replace("calculate", "")
            .strip()
        )

        answer = calculate(expression)

        add_to_history(
            session_id,
            user_message,
            str(answer)
        )

        return {
            "tool": "Calculator",
            "response": str(answer)
        }

    # ---------------- Time ----------------

    if tool == "time":

        answer = current_time()

        add_to_history(
            session_id,
            user_message,
            answer
        )

        return {
            "tool": "Time",
            "response": answer
        }

    # ---------------- RAG ----------------

    if tool == "rag":

        context = search_documents(user_message)

        prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{user_message}
"""

        answer = chat_with_ai(
            prompt,
            history
        )

        add_to_history(
            session_id,
            user_message,
            answer
        )

        return {
            "tool": "RAG",
            "response": answer
        }

    # ---------------- Web Search ----------------

    if tool == "web":

        search_results = web_search(user_message)

        prompt = f"""
You are an AI assistant.

Use ONLY the web search results below to answer the user's question.

Web Search Results:
{search_results}

User Question:
{user_message}

Instructions:
- Give a direct and natural answer.
- Summarize the search results.
- Do not copy all the search snippets.
- Mention important facts only.
- If the search results are empty, say you couldn't find reliable information.
"""

        answer = chat_with_ai(
            prompt,
            history
        )

        add_to_history(
            session_id,
            user_message,
            answer
        )

        return {
            "tool": "Web Search",
            "response": answer
        }

    # ---------------- Normal Chat ----------------

    answer = chat_with_ai(
        user_message,
        history
    )

    add_to_history(
        session_id,
        user_message,
        answer
    )

    return {
        "tool": "Chat",
        "response": answer
    }