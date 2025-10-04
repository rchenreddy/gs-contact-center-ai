#!/usr/bin/env python3
"""
OpenAI-Powered Chatbot
======================

A chatbot that uses OpenAI's GPT models to generate intelligent responses.
Requires an OpenAI API key to function.
"""

import os
from openai import OpenAI
from typing import Optional

# Global OpenAI client
client = None

def setup_openai():
    """
    Set up OpenAI API client with API key.
    
    Returns:
        bool: True if setup successful, False otherwise
    """
    global client
    
    # Get API key from environment variable or user input
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("⚠️  OpenAI API key not found in environment variables.")
        api_key = input("Please enter your OpenAI API key: ").strip()
        
        if not api_key:
            print("❌ No API key provided. Exiting...")
            return False
    
    # Initialize OpenAI client
    try:
        client = OpenAI(api_key=api_key)
        print("✅ OpenAI API key configured successfully!")
        return True
    except Exception as e:
        print(f"❌ Error setting up OpenAI: {e}")
        return False

def get_openai_response(user_message: str) -> Optional[str]:
    """
    Send user message to OpenAI and get AI response.
    
    Args:
        user_message (str): The user's input message
    
    Returns:
        Optional[str]: AI response or None if error occurred
    """
    global client
    
    try:
        # Create the chat completion request using the new API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can change this to "gpt-4" if you have access
            messages=[
                {
                    "role": "system", 
                    "content": "You are a friendly, helpful chatbot. Respond naturally and conversationally, as if talking to a friend. Keep responses concise but engaging."
                },
                {
                    "role": "user", 
                    "content": user_message
                }
            ],
            max_tokens=150,  # Limit response length for terminal chat
            temperature=0.7  # Add some creativity to responses
        )
        
        # Extract the AI's response
        ai_response = response.choices[0].message.content.strip()
        return ai_response
        
    except Exception as e:
        error_msg = str(e)
        if "authentication" in error_msg.lower() or "unauthorized" in error_msg.lower():
            print("❌ Authentication failed. Please check your API key.")
        elif "rate limit" in error_msg.lower():
            print("❌ Rate limit exceeded. Please wait a moment and try again.")
        elif "api" in error_msg.lower():
            print(f"❌ OpenAI API error: {e}")
        else:
            print(f"❌ Unexpected error: {e}")
        return None

def chat_loop():
    """
    Main conversation loop that continues until user types 'bye'.
    """
    print("\n🤖 AI Chatbot is ready! Type 'bye' to end the conversation.")
    print("=" * 50)
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check if user wants to end the conversation
        if user_input.lower() == "bye":
            print("\n🤖 Goodbye! It was great chatting with you! 👋")
            break
        
        # Skip empty inputs
        if not user_input:
            print("🤖 I didn't catch that. What did you say?")
            continue
        
        # Show that we're thinking
        print("🤖 Thinking...")
        
        # Get AI response
        ai_response = get_openai_response(user_input)
        
        if ai_response:
            print(f"🤖 {ai_response}")
        else:
            print("🤖 Sorry, I'm having trouble connecting right now. Please try again.")

def main():
    """
    Main function that sets up and runs the chatbot.
    """
    print("=" * 50)
    print("🤖 Welcome to the OpenAI-Powered Chatbot!")
    print("=" * 50)
    
    # Set up OpenAI API
    if not setup_openai():
        return
    
    # Start the conversation loop
    chat_loop()

if __name__ == "__main__":
    # Check if openai package is installed
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ OpenAI package not found!")
        print("Please install it with: pip install openai")
        exit(1)
    
    # Start the chatbot
    main()
