# app/memory.py

MAX_HISTORY = 10

conversation_memory = {}


def get_history(session_id: str):
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []
    return conversation_memory[session_id]


def add_to_history(session_id: str, user_message: str, assistant_response: str):
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    conversation_memory[session_id].append(
        {
            "user": user_message,
            "assistant": assistant_response
        }
    )

    if len(conversation_memory[session_id]) > MAX_HISTORY:
        conversation_memory[session_id].pop(0)
