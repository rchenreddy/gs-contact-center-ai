# chatbot.py
# Simple Chatbot Simulation for Goldman Sachs Training
# ----------------------------------------------------
# This simulates a contact center bot responding to customer queries.

def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! Welcome to Goldman Sachs support. How can I help you?",
        "account": "I can help you with account-related queries. Could you specify if it's balance or login issues?",
        "loan": "We offer personal, home, and business loans. Would you like interest rate details?",
        "credit card": "Sure! We have multiple credit card options. Do you want to hear about rewards or fees?",
        "bye": "Goodbye! Thanks for connecting with Goldman Sachs."
    }
    return responses.get(user_input.lower(), "I'm sorry, I didn’t understand that. Could you rephrase?")

def main():
    print("🤖 Goldman Sachs Contact Center AI - Chatbot Simulation")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot:", chatbot_response(user_input))
            break
        print("Bot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()





