# Goldman Sachs Contact Center AI

A sophisticated chatbot system designed for Goldman Sachs contact center operations, providing intelligent customer support and query handling with both web API and frontend interfaces.

## 🚀 Features

- **Intelligent Response System**: Pre-configured responses for common banking queries
- **Web API**: RESTful API for integration with web applications
- **Frontend Interface**: React-based web application for user interaction
- **Standalone Mode**: Interactive command-line interface
- **Input Validation**: Security-focused input sanitization and validation
- **Error Handling**: Comprehensive error handling and logging
- **Extensible Design**: Easy to add new responses and functionality
- **Health Monitoring**: Built-in health check endpoints

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Node.js and npm (for frontend development)

## 🛠️ Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd gs-contact-center-ai
   ```

2. **Backend Setup**:
   ```bash
   # Create a virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install Python dependencies
   pip install -r requirements.txt
   ```

3. **Frontend Setup**:
   ```bash
   cd frontend
   npm install
   ```

## 🚀 Usage

### Full Stack Application

1. **Start the backend server**:
   ```bash
   python app.py
   ```
   The server will start on `http://localhost:5000` by default.

2. **Start the frontend development server**:
   ```bash
   cd frontend
   npm start
   ```
   The React app will start on `http://localhost:3000` by default.

### Web API Mode

Start the Flask web server:

```bash
python app.py
```

The server will start on `http://localhost:5000` by default.

#### API Endpoints

- **POST /chat** - Main chat endpoint
  ```bash
  curl -X POST http://localhost:5000/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "hello"}'
  ```

- **GET /health** - Health check
  ```bash
  curl http://localhost:5000/health
  ```

- **GET /responses** - Get all available responses
  ```bash
  curl http://localhost:5000/responses
  ```

#### Example API Usage

```python
import requests

# Send a message to the chatbot
response = requests.post('http://localhost:5000/chat', 
                        json={'message': 'hello'})
print(response.json())
# Output: {"response": "Hi there! Welcome to Goldman Sachs support. How can I help you?", "status": "success"}
```

### Standalone Mode

Run the interactive chatbot:

```bash
python chatbot.py
```

Example interaction:
```
🤖 Goldman Sachs Contact Center AI - Chatbot Simulation
Type 'bye' to exit the conversation.
--------------------------------------------------
You: hello
Bot: Hi there! Welcome to Goldman Sachs support. How can I help you?
You: account
Bot: I can help you with account-related queries. Could you specify if it's balance or login issues?
You: bye
Bot: Goodbye! Thanks for connecting with Goldman Sachs.
```

## 🧪 Testing

Run the test suite:

```bash
# Using unittest (built-in)
python test_chatbot.py

# Using pytest (if installed)
pytest test_chatbot.py -v
```

Run tests with coverage:

```bash
pytest test_chatbot.py --cov=chatbot_core --cov-report=html
```

## 🏗️ Architecture

### Project Structure

```
gs-contact-center-ai/
├── app.py              # Flask web application
├── chatbot.py          # Standalone chatbot interface
├── chatbot_core.py     # Core chatbot logic and functionality
├── test_chatbot.py     # Unit tests
├── requirements.txt    # Python dependencies
├── frontend/           # React frontend application
│   ├── src/           # React source code
│   ├── public/        # Static assets
│   └── package.json   # Node.js dependencies
└── README.md          # This file
```

### Core Components

1. **ChatbotCore Class** (`chatbot_core.py`)
   - Central chatbot logic
   - Input validation and sanitization
   - Response generation
   - Extensible response management

2. **Flask Web App** (`app.py`)
   - RESTful API endpoints
   - Error handling and logging
   - Health monitoring
   - Production-ready configuration
   - CORS support for frontend integration

3. **React Frontend** (`frontend/`)
   - Modern web interface
   - Real-time chat interface
   - Responsive design
   - Integration with Flask backend

4. **Standalone Interface** (`chatbot.py`)
   - Interactive command-line interface
   - User-friendly conversation flow
   - Error handling for user interactions

## ⚙️ Configuration

### Environment Variables

- `FLASK_DEBUG`: Set to `True` for debug mode (default: `False`)
- `PORT`: Server port (default: `5000`)
- `HOST`: Server host (default: `0.0.0.0`)

### Example Configuration

```bash
export FLASK_DEBUG=False
export PORT=8080
export HOST=127.0.0.1
python app.py
```

## 🔒 Security Features

- **Input Validation**: Comprehensive input sanitization
- **XSS Protection**: Detection and blocking of script injection attempts
- **Length Limits**: Protection against extremely long inputs
- **Error Handling**: Secure error messages without information leakage
- **CORS Configuration**: Secure cross-origin resource sharing

## 📈 Extending the Chatbot

### Adding New Responses

```python
from chatbot_core import chatbot

# Add a new response
chatbot.add_response("investment", "We offer various investment products. Would you like to know about stocks, bonds, or mutual funds?")
```

### Custom Response Logic

You can extend the `ChatbotCore` class to add custom logic:

```python
class CustomChatbot(ChatbotCore):
    def get_response(self, user_input):
        # Add custom logic here
        response = super().get_response(user_input)
        # Modify response if needed
        return response
```

## 🚀 Production Deployment

### Using Gunicorn

1. Install Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Run with Gunicorn:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## 📝 License

This project is for educational and training purposes as part of Goldman Sachs contact center AI development.

## 🆘 Support

For questions or issues:
1. Check the test suite for expected behavior
2. Review the API documentation above
3. Check the logs for error messages
4. Ensure all dependencies are installed correctly

## 🔄 Version History

- **v1.0.0**: Initial release with basic chatbot functionality
- **v1.1.0**: Added comprehensive error handling and input validation
- **v1.2.0**: Implemented modular architecture and extensive testing
- **v1.3.0**: Added React frontend interface and CORS support