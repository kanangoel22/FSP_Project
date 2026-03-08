from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, static_folder="static", template_folder="templates")

RASA_API_URL = "http://127.0.0.1:5005/webhooks/rest/webhook"


@app.route("/")
def home():
    """Serve the chatbot web interface."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Proxy endpoint: forwards user message to Rasa and returns bot response."""
    user_message = request.json.get("message", "")
    sender = request.json.get("sender", "user")

    if not user_message.strip():
        return jsonify([{"text": "Please type a message."}])

    try:
        rasa_response = requests.post(
            RASA_API_URL,
            json={"sender": sender, "message": user_message},
            timeout=30,
        )
        rasa_response.raise_for_status()
        bot_responses = rasa_response.json()

        if not bot_responses:
            return jsonify([{"text": "I didn't catch that. Try asking for a motivational, funny, or love quote!"}])

        return jsonify(bot_responses)

    except requests.exceptions.ConnectionError:
        return jsonify([{"text": "Could not connect to the chatbot server. Make sure Rasa is running."}]), 503
    except requests.exceptions.Timeout:
        return jsonify([{"text": "The server took too long to respond. Please try again."}]), 504
    except Exception as e:
        return jsonify([{"text": f"Something went wrong: {str(e)}"}]), 500


if __name__ == "__main__":
    print("=" * 50)
    print("  Quote Bot Web Interface")
    print("  Open http://localhost:5000 in your browser")
    print("=" * 50)
    app.run(debug=True, port=5000)
