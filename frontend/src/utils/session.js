function generateId() {
  if (window.crypto && typeof window.crypto.randomUUID === "function") {
    return window.crypto.randomUUID();
  }

  return Math.random().toString(36).substring(2) + Date.now().toString(36);
}

export function getSessionId() {
  let sessionId = localStorage.getItem("session_id");

  if (!sessionId) {
    sessionId = generateId();
    localStorage.setItem("session_id", sessionId);
  }

  return sessionId;
}

export function createNewSession() {
  const sessionId = generateId();
  localStorage.setItem("session_id", sessionId);
  return sessionId;
}
