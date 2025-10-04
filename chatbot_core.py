"""
Chatbot Core Module for Goldman Sachs Contact Center AI
======================================================

This module contains the core chatbot logic and response handling.
"""

from typing import Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChatbotCore:
    """
    Core chatbot functionality for Goldman Sachs contact center.
    
    This class handles the main chatbot logic including response generation,
    input validation, and conversation management.
    """
    
    def __init__(self):
        """Initialize the chatbot with predefined responses."""
        self.responses = {
            "hello": "Hi there! Welcome to Goldman Sachs support. How can I help you?",
            "account": "I can help you with account-related queries. Could you specify if it's balance or login issues?",
            "loan": "We offer personal, home, and business loans. Would you like interest rate details?",
            "credit card": "Sure! We have multiple credit card options. Do you want to hear about rewards or fees?",
            "bye": "Goodbye! Thanks for connecting with Goldman Sachs."
        }
        logger.info("ChatbotCore initialized with {} predefined responses".format(len(self.responses)))
    
    def validate_input(self, user_input: str) -> bool:
        """
        Validate user input for basic sanity checks.
        
        Args:
            user_input (str): The user's input message
            
        Returns:
            bool: True if input is valid, False otherwise
        """
        if not user_input or not isinstance(user_input, str):
            return False
        
        # Check for reasonable length (not too short or too long)
        if len(user_input.strip()) < 1 or len(user_input) > 1000:
            return False
        
        # Check for potentially harmful content (basic check)
        dangerous_patterns = ['<script', 'javascript:', 'data:', 'vbscript:']
        user_input_lower = user_input.lower()
        for pattern in dangerous_patterns:
            if pattern in user_input_lower:
                logger.warning(f"Potentially dangerous input detected: {pattern}")
                return False
        
        return True
    
    def get_response(self, user_input: str) -> str:
        """
        Generate a response for the given user input.
        
        Args:
            user_input (str): The user's input message
            
        Returns:
            str: The chatbot's response
        """
        try:
            # Validate input
            if not self.validate_input(user_input):
                logger.warning(f"Invalid input received: {user_input[:50]}...")
                return "I'm sorry, I didn't understand that. Could you please rephrase your question?"
            
            # Clean and normalize input
            cleaned_input = user_input.lower().strip()
            
            # Get response from predefined responses
            response = self.responses.get(cleaned_input, None)
            
            if response:
                logger.info(f"Found predefined response for: {cleaned_input}")
                return response
            else:
                logger.info(f"No predefined response found for: {cleaned_input}")
                return "I'm sorry, I didn't understand that. Could you rephrase?"
                
        except Exception as e:
            logger.error(f"Error processing user input: {str(e)}")
            return "I'm sorry, I'm experiencing technical difficulties. Please try again later."
    
    def add_response(self, key: str, response: str) -> bool:
        """
        Add a new response to the chatbot's knowledge base.
        
        Args:
            key (str): The trigger phrase
            response (str): The response to give
            
        Returns:
            bool: True if successfully added, False otherwise
        """
        try:
            if not key or not response:
                return False
            
            self.responses[key.lower()] = response
            logger.info(f"Added new response for key: {key}")
            return True
        except Exception as e:
            logger.error(f"Error adding response: {str(e)}")
            return False
    
    def get_available_responses(self) -> Dict[str, str]:
        """
        Get all available responses.
        
        Returns:
            Dict[str, str]: Dictionary of all responses
        """
        return self.responses.copy()


# Create a global instance for easy import
chatbot = ChatbotCore()
