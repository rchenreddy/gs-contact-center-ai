from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! Welcome to Goldman Sachs support. How can I help you?",
        "account": "I can help you with account-related queries. Could you specify if it's balance or login issues?",
        "loan": "We offer personal, home, and business loans. Would you like interest rate details?",
        "credit card": "Sure! We have multiple credit card options. Do you want to hear about rewards or fees?",
        "bye": "Goodbye! Thanks for connecting with Goldman Sachs."
    }
    return responses.get(user_input.lower(), "I'm sorry, I didn’t understand that. Could you rephrase?")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = chatbot_response(user_input)
    return jsonify({"user": user_input, "bot": response})

if __name__ == "__main__":
    app.run(debug=True)

