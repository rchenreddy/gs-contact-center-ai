#!/usr/bin/env python3
"""
Casual Chatbot - Human-Style Conversation
=========================================

A simple chatbot that mimics natural human conversation.
Responds to greetings, asks how you are, and keeps the chat flowing.
"""

def main():
    """
    Main function that runs the casual conversation loop.
    """
    print("=" * 40)
    print("💬 Hey there! I'm your casual chat buddy!")
    print("Type 'bye' whenever you want to end our conversation.")
    print("=" * 40)
    
    # Start the conversation loop
    chat_loop()

def chat_loop():
    """
    The main conversation loop that continues until user says 'bye'.
    """
    while True:
        # Get user input and clean it up
        user_input = input("\nYou: ").strip().lower()
        
        # Check if user wants to end the conversation
        if user_input == "bye":
            say_goodbye()
            break
        
        # Process the user's message and get bot response
        bot_response = get_response(user_input)
        print(f"Bot: {bot_response}")

def get_response(user_input):
    """
    Generate an appropriate response based on user input.
    
    Args:
        user_input (str): The user's message (already converted to lowercase)
    
    Returns:
        str: The bot's response
    """
    # Handle empty input
    if not user_input:
        return "I didn't catch that. What did you say?"
    
    # Check for greetings
    greetings = ["hi", "hello", "hey", "hiya", "howdy"]
    if any(greeting in user_input for greeting in greetings):
        return "Hey there! Nice to chat with you! 😊"
    
    # Check for "how are you" variations
    how_are_you_phrases = ["how are you", "how are you doing", "how's it going", "how do you do"]
    if any(phrase in user_input for phrase in how_are_you_phrases):
        return "I'm doing great, thanks for asking! How about you?"
    
    # Check for positive responses about being good/fine
    good_responses = ["i am good", "i'm good", "i am fine", "i'm fine", "doing well", "i'm well", "i am well"]
    if any(response in user_input for response in good_responses):
        return "That's awesome! 😊"
    
    # Check for other positive responses
    other_good = ["good", "great", "awesome", "wonderful", "excellent", "fantastic"]
    if any(word in user_input for word in other_good):
        return "Glad to hear that! 😊"
    
    # Check for negative responses
    negative_responses = ["bad", "terrible", "awful", "not good", "not well", "sad", "tired"]
    if any(word in user_input for word in negative_responses):
        return "Oh no, sorry to hear that. Hope things get better soon! 💙"
    
    # Default response for anything else
    return "Hmm, interesting! Tell me more..."

def say_goodbye():
    """
    Handle the goodbye conversation ending.
    """
    print("\nBot: It was really nice chatting with you!")
    print("Bot: Take care and have a wonderful day! 👋")
    print("=" * 40)

if __name__ == "__main__":
    # Start the casual chatbot
    main()

