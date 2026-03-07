const chatbox = document.getElementById("chatbox");
const inputField = document.getElementById("userMsg");
const typingIndicator = document.getElementById("typing-indicator");
const sendBtn = document.getElementById("sendBtn");
const clearBtn = document.getElementById("clearBtn");

// Send on click or Enter
sendBtn.addEventListener("click", sendMessage);
inputField.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
});

// Clear chat
clearBtn.addEventListener("click", () => {
    chatbox.innerHTML = "";
    addWelcome();
});

// Quick-action chips
document.addEventListener("click", (e) => {
    if (e.target.classList.contains("chip")) {
        const msg = e.target.getAttribute("data-msg");
        if (msg) {
            inputField.value = msg;
            sendMessage();
        }
    }
});

async function sendMessage() {
    const input = inputField.value.trim();
    if (!input) return;

    // Remove welcome if present
    const welcome = chatbox.querySelector(".welcome-message");
    if (welcome) welcome.remove();

    // User message
    appendMessage(input, "user-msg");
    inputField.value = "";
    inputField.focus();
    scrollToBottom();

    // Show typing
    typingIndicator.classList.remove("hidden");
    scrollToBottom();

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sender: "user", message: input }),
        });

        const data = await response.json();
        typingIndicator.classList.add("hidden");

        if (data && data.length > 0) {
            data.forEach((msg, i) => {
                setTimeout(() => {
                    appendMessage(msg.text, "bot-msg");
                    scrollToBottom();
                }, i * 300);
            });
        } else {
            appendMessage("Hmm, I don't have a response for that. Try asking for a quote!", "bot-msg");
        }
    } catch (error) {
        typingIndicator.classList.add("hidden");
        appendMessage("Could not connect to the server. Please make sure Rasa is running.", "bot-msg");
    }

    scrollToBottom();
}

function appendMessage(text, className) {
    const div = document.createElement("div");
    div.className = `msg ${className}`;
    div.textContent = text;
    chatbox.appendChild(div);
}

function scrollToBottom() {
    setTimeout(() => {
        chatbox.scrollTop = chatbox.scrollHeight;
    }, 50);
}

function addWelcome() {
    chatbox.innerHTML = `
        <div class="welcome-message">
            <div class="welcome-icon">&#10024;</div>
            <h2>Welcome to Quote Bot!</h2>
            <p>I can share quotes to brighten your day. Try one of these:</p>
            <div class="quick-actions">
                <button class="chip" data-msg="Give me a motivational quote">Motivation</button>
                <button class="chip" data-msg="Inspire me">Inspiration</button>
                <button class="chip" data-msg="Tell me a joke">Funny</button>
                <button class="chip" data-msg="Give me a love quote">Love</button>
                <button class="chip" data-msg="How to be successful">Success</button>
            </div>
        </div>
    `;
}
