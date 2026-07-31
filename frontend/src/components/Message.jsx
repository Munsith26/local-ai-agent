import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneLight } from "react-syntax-highlighter/dist/esm/styles/prism";

import {
  FiCopy,
  FiCheck,
  FiCpu,
  FiClock,
  FiSearch,
  FiMessageSquare,
} from "react-icons/fi";

import { useState } from "react";

import "../styles/message.css";

function Message({ sender, text, tool }) {
  const isUser = sender === "user";

  const [copied, setCopied] = useState(false);

  const copyText = async () => {
    await navigator.clipboard.writeText(text);

    setCopied(true);

    setTimeout(() => {
      setCopied(false);
    }, 2000);
  };

  const getToolIcon = () => {
    switch (tool) {
      case "calculator":
        return <FiCpu />;

      case "time":
        return <FiClock />;

      case "rag":
        return <FiSearch />;

      default:
        return <FiMessageSquare />;
    }
  };

  return (
    <div className={`message-row ${isUser ? "user" : "ai"}`}>
      <div className="message-card">
        <div className="message-header">
          <div className="author">{isUser ? "👤 You" : "🤖 AI Assistant"}</div>

          {!isUser && (
            <div className="header-actions">
              <span className="tool-chip">
                {getToolIcon()}
                {tool || "chat"}
              </span>

              <button className="copy-btn" onClick={copyText}>
                {copied ? <FiCheck /> : <FiCopy />}
              </button>
            </div>
          )}
        </div>

        <div className="message-content">
          {isUser ? (
            text
          ) : (
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                code({ inline, className, children, ...props }) {
                  const match = /language-(\w+)/.exec(className || "");

                  return !inline && match ? (
                    <SyntaxHighlighter
                      style={oneLight}
                      language={match[1]}
                      PreTag="div"
                    >
                      {String(children).replace(/\n$/, "")}
                    </SyntaxHighlighter>
                  ) : (
                    <code className={className}>{children}</code>
                  );
                },
              }}
            >
              {text}
            </ReactMarkdown>
          )}
        </div>
      </div>
    </div>
  );
}

export default Message;
