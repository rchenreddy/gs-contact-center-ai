"""
Flask Web Application for Goldman Sachs Contact Center AI
=======================================================

This module provides the web API for the contact center chatbot.
"""

from flask import Flask, request, jsonify
from chatbot_core import chatbot
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
app.config['JSON_SORT_KEYS'] = False

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        "status": "healthy",
        "service": "Goldman Sachs Contact Center AI",
        "version": "1.0.0"
    })

@app.route("/chat", methods=["POST"])
def chat():
    """
    Main chat endpoint for processing user messages.
    
    Expected JSON payload:
    {
        "message": "user input string"
    }
    
    Returns:
        JSON response with chatbot reply
    """
    try:
        # Validate request
        if not request.is_json:
            logger.warning("Request is not JSON")
            return jsonify({
                "error": "Content-Type must be application/json"
            }), 400
        
        # Get JSON data
        data = request.get_json()
        if not data:
            logger.warning("Empty JSON payload received")
            return jsonify({
                "error": "Empty request body"
            }), 400
        
        # Extract message
        user_input = data.get("message", "")
        if not user_input:
            logger.warning("No message provided in request")
            return jsonify({
                "error": "Message field is required"
            }), 400
        
        # Get chatbot response
        response = chatbot.get_response(user_input)
        
        logger.info(f"Processed message: {user_input[:50]}...")
        
        return jsonify({
            "response": response,
            "status": "success"
        })
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "status": "error"
        }), 500

@app.route("/responses", methods=["GET"])
def get_responses():
    """Get all available chatbot responses (for debugging/admin purposes)."""
    try:
        responses = chatbot.get_available_responses()
        return jsonify({
            "responses": responses,
            "count": len(responses)
        })
    except Exception as e:
        logger.error(f"Error getting responses: {str(e)}")
        return jsonify({
            "error": "Internal server error"
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        "error": "Endpoint not found",
        "available_endpoints": ["/chat", "/health", "/responses"]
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors."""
    return jsonify({
        "error": "Method not allowed"
    }), 405

if __name__ == "__main__":
    # Get configuration from environment variables
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'True'
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')
    
    logger.info(f"Starting Goldman Sachs Contact Center AI on {host}:{port}")
    logger.info(f"Debug mode: {debug_mode}")
    
    app.run(host=host, port=port, debug=debug_mode)


