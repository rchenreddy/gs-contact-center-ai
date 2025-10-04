"""
Standalone Chatbot Simulation for Goldman Sachs Training
=======================================================

This simulates a contact center bot responding to customer queries.
Uses the chatbot_core module for consistent behavior.
"""

from chatbot_core import chatbot
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Main function to run the interactive chatbot simulation."""
    print("🤖 Goldman Sachs Contact Center AI - Chatbot Simulation")
    print("Type 'bye' to exit the conversation.")
    print("-" * 50)
    
    try:
        while True:
            user_input = input("You: ")
            
            # Check for exit condition
            if user_input.lower() == "bye":
                response = chatbot.get_response(user_input)
                print("Bot:", response)
                break
            
            # Get and display response
            response = chatbot.get_response(user_input)
            print("Bot:", response)
            
    except KeyboardInterrupt:
        print("\n\nGoodbye! Thanks for using Goldman Sachs Contact Center AI.")
    except Exception as e:
        logger.error(f"Error in main chatbot loop: {str(e)}")
        print("Sorry, I encountered an error. Please try again.")

if __name__ == "__main__":
    main()





