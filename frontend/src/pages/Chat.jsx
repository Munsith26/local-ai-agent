import { useState } from "react";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

import API from "../services/api";
import { getSessionId, createNewSession } from "../utils/session";

function Chat() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState(getSessionId());

  // Send message
  const sendMessage = async (text) => {
    if (!text.trim()) return;

    // Add user message
    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text,
      },
    ]);

    setLoading(true);

    try {
      const response = await API.post("/chat", {
        session_id: sessionId,
        message: text,
      });

      // Add AI response
      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: response.data.response,
          tool: response.data.tool,
        },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "Unable to connect to AI.",
        },
      ]);

      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Start a new chat
  const handleNewChat = () => {
    const id = createNewSession();
    setSessionId(id);
    setMessages([]);
  };

  // Clear chat history
  const handleClear = async () => {
    try {
      await API.delete(`/history/${sessionId}`);
      setMessages([]);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="layout">
      <Sidebar onNewChat={handleNewChat} />

      <main className="main-content">
        <div className="chat-container">
          <ChatWindow messages={messages} loading={loading} />
        </div>

        <ChatInput
          onSend={sendMessage}
          onNewChat={handleNewChat}
          onClear={handleClear}
          isWelcome={messages.length === 0}
        />
      </main>
    </div>
  );
}

export default Chat;
