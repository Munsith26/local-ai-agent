import "../styles/sidebar.css";

function Sidebar({ onNewChat }) {
  return (
    <aside className="sidebar">
      <div>
        <div className="logo">
          <div className="logo-circle">🤖</div>

          <div>
            <h2>Local AI</h2>

            <span>Workspace</span>
          </div>
        </div>

        <button className="new-chat-btn" onClick={onNewChat}>
          + New Chat
        </button>

        <div className="menu">
          <p className="menu-title">Recent</p>

          <button className="menu-item">💬 Chat 1</button>

          <button className="menu-item">💬 Chat 2</button>

          <button className="menu-item">💬 Chat 3</button>
        </div>
      </div>

      <div className="bottom-menu">
        <button className="menu-item">⚙ Settings</button>
      </div>
    </aside>
  );
}

export default Sidebar;
