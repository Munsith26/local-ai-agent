import { useState } from "react";
import "../styles/input.css";

function ChatInput({ onSend, onNewChat, onClear, isWelcome }) {
  const [message, setMessage] = useState("");

  const send = () => {
    if (!message.trim()) return;

    onSend(message);
    setMessage("");
  };

  return (
    <div className={`input-wrapper ${isWelcome ? "welcome-mode" : ""}`}>
      <div className="chat-input">
        <input
          type="text"
          placeholder="Ask anything..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") send();
          }}
        />

        <button onClick={send}>➜</button>
      </div>

      {isWelcome && (
        <div className="quick-actions">
          <button className="pill-btn" onClick={onNewChat}>
            + New Chat
          </button>

          <button className="pill-btn" onClick={onClear}>
            🗑 Clear
          </button>
        </div>
      )}
    </div>
  );
}

export default ChatInput;
