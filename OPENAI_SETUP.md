# OpenAI Chatbot Setup Guide

## Prerequisites

1. **OpenAI API Key**: You need an API key from OpenAI
   - Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
   - Create a new API key
   - Copy the key (it starts with `sk-`)

## Setup Instructions

### Method 1: Environment Variable (Recommended)

1. **Set your API key as an environment variable**:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

2. **Add to your shell profile** (to make it permanent):
   ```bash
   echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.zshrc
   source ~/.zshrc
   ```

### Method 2: Enter Key When Prompted

If you don't set the environment variable, the chatbot will ask for your API key when you run it.

## Running the Chatbot

1. **Activate your virtual environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Run the chatbot**:
   ```bash
   python openai_chatbot.py
   ```

## Example Conversation

```
🤖 Welcome to the OpenAI-Powered Chatbot!
✅ OpenAI API key configured successfully!

🤖 AI Chatbot is ready! Type 'bye' to end the conversation.

You: Hello! How are you today?
🤖 Thinking...
🤖 Hello! I'm doing great, thank you for asking! I'm here and ready to help with whatever you'd like to chat about. How are you doing today?

You: What's the weather like?
🤖 Thinking...
🤖 I don't have access to real-time weather data, but I'd be happy to help you find current weather information! You could check a weather app, website, or ask a voice assistant for the most up-to-date forecast in your area. Is there anything else I can help you with?

You: bye
🤖 Goodbye! It was great chatting with you! 👋
```

## Configuration Options

You can modify the chatbot by editing `openai_chatbot.py`:

- **Model**: Change `gpt-3.5-turbo` to `gpt-4` (if you have access)
- **Max tokens**: Adjust response length (currently 150)
- **Temperature**: Control creativity (0.7 = balanced)
- **System prompt**: Modify the bot's personality

## Troubleshooting

### Common Issues:

1. **"Authentication failed"**: Check your API key
2. **"Rate limit exceeded"**: You've hit OpenAI's rate limits
3. **"Package not found"**: Run `pip install openai`
4. **Empty responses**: Check your internet connection

### Cost Considerations:

- GPT-3.5-turbo is very affordable (~$0.002 per 1K tokens)
- GPT-4 costs more but provides better responses
- Monitor your usage in the OpenAI dashboard

## Security Notes

- Never share your API key publicly
- Don't commit API keys to version control
- Use environment variables for production
