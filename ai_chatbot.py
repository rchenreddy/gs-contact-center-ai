#!/usr/bin/env python3
"""
AI-Powered Chatbot using OpenAI API
===================================

A terminal-based chatbot that uses OpenAI's GPT models for intelligent responses.
Features comprehensive error handling and natural conversation flow.
"""

import os
import sys
from openai import OpenAI
from typing import Optional

class AIChatbot:
    """
    A chatbot class that handles OpenAI API interactions.
    """
    
    def __init__(self):
        """Initialize the chatbot with OpenAI client."""
        self.client = None
        self.conversation_history = []
        
    def setup_api_key(self) -> bool:
        """
        Set up the OpenAI API key and initialize the client.
        
        Returns:
            bool: True if setup successful, False otherwise
        """
        # Try to get API key from environment variable first
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            print("🔑 OpenAI API key not found in environment variables.")
            print("You can:")
            print("1. Set it as environment variable: export OPENAI_API_KEY='your-key-here'")
            print("2. Enter it now (will be used for this session only)")
            
            api_key = input("\nEnter your OpenAI API key: ").strip()
            
            if not api_key:
                print("❌ No API key provided. Exiting...")
                return False
        
        # Validate API key format
        if not api_key.startswith('sk-'):
            print("❌ Invalid API key format. OpenAI keys should start with 'sk-'")
            return False
        
        try:
            # Initialize OpenAI client
            self.client = OpenAI(api_key=api_key)
            print("✅ OpenAI client initialized successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Error initializing OpenAI client: {e}")
            return False
    
    def get_ai_response(self, user_message: str) -> Optional[str]:
        """
        Send user message to OpenAI and get AI response.
        
        Args:
            user_message (str): The user's input message
            
        Returns:
            Optional[str]: AI response or None if error occurred
        """
        try:
            # Create conversation context
            messages = [
                {
                    "role": "system",
                    "content": "You are a friendly, helpful AI assistant. Respond naturally and conversationally, as if talking to a friend. Keep responses concise but engaging. Be helpful and positive."
                }
            ]
            
            # Add conversation history for context
            messages.extend(self.conversation_history[-6:])  # Keep last 6 messages for context
            
            # Add current user message
            messages.append({"role": "user", "content": user_message})
            
            # Send request to OpenAI
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",  # You can change to "gpt-4" if you have access
                messages=messages,
                max_tokens=200,  # Limit response length
                temperature=0.7,  # Add some creativity
                timeout=30  # 30 second timeout
            )
            
            # Extract AI response
            ai_response = response.choices[0].message.content.strip()
            
            # Update conversation history
            self.conversation_history.append({"role": "user", "content": user_message})
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            return ai_response
            
        except Exception as e:
            # Handle different types of errors
            error_msg = str(e).lower()
            
            if "authentication" in error_msg or "unauthorized" in error_msg or "invalid" in error_msg:
                print("❌ Authentication failed. Please check your API key.")
            elif "rate limit" in error_msg or "quota" in error_msg:
                print("❌ Rate limit exceeded. You may have hit your usage limits.")
            elif "timeout" in error_msg:
                print("❌ Request timed out. Please try again.")
            elif "network" in error_msg or "connection" in error_msg:
                print("❌ Network error. Please check your internet connection.")
            else:
                print(f"❌ API Error: {e}")
            
            return None
    
    def start_conversation(self):
        """
        Start the main conversation loop.
        """
        print("\n" + "="*50)
        print("🤖 AI Chatbot is ready to chat!")
        print("Type 'bye' to end the conversation")
        print("="*50)
        
        while True:
            try:
                # Get user input
                user_input = input("\n👤 You: ").strip()
                
                # Check if user wants to end conversation
                if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
                    self.end_conversation()
                    break
                
                # Skip empty inputs
                if not user_input:
                    print("🤖 I didn't catch that. What did you say?")
                    continue
                
                # Show that we're processing
                print("🤖 Thinking...", end="", flush=True)
                
                # Get AI response
                ai_response = self.get_ai_response(user_input)
                
                # Clear the "Thinking..." message
                print("\r" + " " * 20 + "\r", end="", flush=True)
                
                if ai_response:
                    print(f"🤖 AI: {ai_response}")
                else:
                    print("🤖 Sorry, I'm having trouble connecting right now. Please try again.")
                    
            except KeyboardInterrupt:
                # Handle Ctrl+C gracefully
                print("\n\n🤖 Chat interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Unexpected error: {e}")
                print("🤖 Let's try again...")
    
    def end_conversation(self):
        """
        End the conversation with a friendly goodbye.
        """
        print("\n🤖 It was great chatting with you!")
        print("🤖 Take care and have a wonderful day! 👋")
        print("="*50)

def main():
    """
    Main function to run the AI chatbot.
    """
    print("="*50)
    print("🤖 Welcome to the AI-Powered Chatbot!")
    print("="*50)
    
    # Check if OpenAI package is installed
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ OpenAI package not found!")
        print("Please install it with: pip install openai")
        sys.exit(1)
    
    # Create and initialize chatbot
    chatbot = AIChatbot()
    
    # Set up API key
    if not chatbot.setup_api_key():
        print("\n💡 To get an API key:")
        print("1. Go to https://platform.openai.com/api-keys")
        print("2. Sign in to your OpenAI account")
        print("3. Create a new API key")
        print("4. Set it as environment variable: export OPENAI_API_KEY='your-key'")
        sys.exit(1)
    
    # Start the conversation
    chatbot.start_conversation()

if __name__ == "__main__":
    main()
