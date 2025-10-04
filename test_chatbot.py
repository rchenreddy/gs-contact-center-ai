"""
Unit Tests for Goldman Sachs Contact Center AI
==============================================

This module contains comprehensive unit tests for the chatbot functionality.
"""

import unittest
import sys
import os

# Add the current directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot_core import ChatbotCore
import json


class TestChatbotCore(unittest.TestCase):
    """Test cases for the ChatbotCore class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.chatbot = ChatbotCore()
    
    def test_initialization(self):
        """Test that the chatbot initializes correctly."""
        self.assertIsInstance(self.chatbot.responses, dict)
        self.assertGreater(len(self.chatbot.responses), 0)
        self.assertIn("hello", self.chatbot.responses)
        self.assertIn("bye", self.chatbot.responses)
    
    def test_validate_input_valid_cases(self):
        """Test input validation with valid inputs."""
        valid_inputs = [
            "hello",
            "account",
            "loan",
            "credit card",
            "bye",
            "Hello World",
            "How can I help you?",
            "a" * 100,  # 100 character string
        ]
        
        for input_text in valid_inputs:
            with self.subTest(input_text=input_text):
                self.assertTrue(self.chatbot.validate_input(input_text))
    
    def test_validate_input_invalid_cases(self):
        """Test input validation with invalid inputs."""
        invalid_inputs = [
            "",  # Empty string
            None,  # None value
            123,  # Non-string type
            "a" * 1001,  # Too long
            "<script>alert('xss')</script>",  # XSS attempt
            "javascript:alert('xss')",  # JavaScript injection
            "data:text/html,<script>alert('xss')</script>",  # Data URI XSS
        ]
        
        for input_text in invalid_inputs:
            with self.subTest(input_text=input_text):
                self.assertFalse(self.chatbot.validate_input(input_text))
    
    def test_get_response_known_inputs(self):
        """Test responses for known inputs."""
        test_cases = [
            ("hello", "Hi there! Welcome to Goldman Sachs support. How can I help you?"),
            ("account", "I can help you with account-related queries. Could you specify if it's balance or login issues?"),
            ("loan", "We offer personal, home, and business loans. Would you like interest rate details?"),
            ("credit card", "Sure! We have multiple credit card options. Do you want to hear about rewards or fees?"),
            ("bye", "Goodbye! Thanks for connecting with Goldman Sachs."),
        ]
        
        for input_text, expected_response in test_cases:
            with self.subTest(input_text=input_text):
                response = self.chatbot.get_response(input_text)
                self.assertEqual(response, expected_response)
    
    def test_get_response_case_insensitive(self):
        """Test that responses are case insensitive."""
        test_cases = [
            "HELLO",
            "Hello",
            "HELLO WORLD",
            "Account",
            "ACCOUNT",
            "Bye",
            "BYE",
        ]
        
        for input_text in test_cases:
            with self.subTest(input_text=input_text):
                response = self.chatbot.get_response(input_text)
                self.assertIsInstance(response, str)
                self.assertGreater(len(response), 0)
    
    def test_get_response_unknown_inputs(self):
        """Test responses for unknown inputs."""
        unknown_inputs = [
            "random text",
            "help me",
            "what is this",
            "unknown query",
        ]
        
        for input_text in unknown_inputs:
            with self.subTest(input_text=input_text):
                response = self.chatbot.get_response(input_text)
                self.assertIn("I'm sorry, I didn't understand", response)
    
    def test_get_response_invalid_input(self):
        """Test responses for invalid inputs."""
        # Test empty string
        response = self.chatbot.get_response("")
        self.assertIn("I'm sorry, I didn't understand", response)
        
        # Test None input (should trigger technical difficulties message)
        response = self.chatbot.get_response(None)
        self.assertIn("I'm sorry, I'm experiencing technical difficulties", response)
        
        # Test XSS attempt
        response = self.chatbot.get_response("<script>alert('xss')</script>")
        self.assertIn("I'm sorry, I didn't understand", response)
    
    def test_add_response(self):
        """Test adding new responses."""
        # Test successful addition
        result = self.chatbot.add_response("test", "This is a test response")
        self.assertTrue(result)
        self.assertEqual(self.chatbot.get_response("test"), "This is a test response")
        
        # Test case insensitive addition
        result = self.chatbot.add_response("TEST2", "Another test response")
        self.assertTrue(result)
        self.assertEqual(self.chatbot.get_response("test2"), "Another test response")
    
    def test_add_response_invalid(self):
        """Test adding invalid responses."""
        # Test with empty key
        result = self.chatbot.add_response("", "response")
        self.assertFalse(result)
        
        # Test with None key
        result = self.chatbot.add_response(None, "response")
        self.assertFalse(result)
        
        # Test with empty response
        result = self.chatbot.add_response("key", "")
        self.assertFalse(result)
    
    def test_get_available_responses(self):
        """Test getting all available responses."""
        responses = self.chatbot.get_available_responses()
        self.assertIsInstance(responses, dict)
        self.assertGreater(len(responses), 0)
        
        # Test that it returns a copy, not the original
        original_count = len(self.chatbot.responses)
        responses["new_key"] = "new_value"
        self.assertEqual(len(self.chatbot.responses), original_count)


class TestChatbotIntegration(unittest.TestCase):
    """Integration tests for the chatbot system."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.chatbot = ChatbotCore()
    
    def test_conversation_flow(self):
        """Test a typical conversation flow."""
        conversation = [
            ("hello", "Hi there! Welcome to Goldman Sachs support. How can I help you?"),
            ("account", "I can help you with account-related queries. Could you specify if it's balance or login issues?"),
            ("loan", "We offer personal, home, and business loans. Would you like interest rate details?"),
            ("bye", "Goodbye! Thanks for connecting with Goldman Sachs."),
        ]
        
        for user_input, expected_response in conversation:
            with self.subTest(user_input=user_input):
                response = self.chatbot.get_response(user_input)
                self.assertEqual(response, expected_response)
    
    def test_error_handling(self):
        """Test error handling in various scenarios."""
        # Test with extremely long input
        long_input = "a" * 2000
        response = self.chatbot.get_response(long_input)
        self.assertIn("I'm sorry, I didn't understand", response)
        
        # Test with special characters
        special_input = "!@#$%^&*()"
        response = self.chatbot.get_response(special_input)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
