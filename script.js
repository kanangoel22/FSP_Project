const chatbox = document.getElementById("chatbox");
const inputField = document.getElementById("userMsg");
const typingIndicator = document.getElementById("typing-indicator");

document.getElementById("sendBtn").addEventListener("click", sendMessage);
inputField.addEventListener("keypress", (e) => { if (e.key === 'Enter') sendMessage(); });

async function sendMessage() {
    const input = inputField.value.trim();
    if (!input) return;

    // User Message
    chatbox.innerHTML += `<div class="msg user-msg">${input}</div>`;
    inputField.value = "";
    chatbox.scrollTop = chatbox.scrollHeight;

    // Show typing state
    typingIndicator.classList.remove("hidden");

    try {
        const response = await fetch("http://localhost:5005/webhooks/rest/webhook", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ "sender": "user", "message": input })
        });

        const data = await response.json();
        typingIndicator.classList.add("hidden");

        data.forEach(msg => {
            chatbox.innerHTML += `<div class="msg bot-msg">${msg.text}</div>`;
        });
    } catch (error) {
        typingIndicator.classList.add("hidden");
        chatbox.innerHTML += `<div class="msg bot-msg">System error: Unable to connect.</div>`;
    }
    chatbox.scrollTop = chatbox.scrollHeight;
}