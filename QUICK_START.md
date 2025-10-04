# AI Chatbot Quick Start Guide

## 🚀 Getting Started

### 1. Get Your OpenAI API Key
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Sign in to your account (create one if needed)
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

### 2. Set Up Your API Key

**Option A: Environment Variable (Recommended)**
```bash
export OPENAI_API_KEY="sk-your-actual-key-here"
```

**Option B: Enter When Prompted**
Just run the script and enter your key when asked.

### 3. Run the Chatbot
```bash
python ai_chatbot.py
```

## 💬 Example Conversation

```
🤖 Welcome to the AI-Powered Chatbot!
✅ OpenAI client initialized successfully!

🤖 AI Chatbot is ready to chat!
Type 'bye' to end the conversation

👤 You: Hello! How are you today?
🤖 AI: Hello! I'm doing great, thank you for asking! I'm here and ready to help with whatever you'd like to chat about. How are you doing today?

👤 You: What's the weather like?
🤖 AI: I don't have access to real-time weather data, but I can help you find weather information! You could check your local weather app, visit a weather website like Weather.com, or ask a voice assistant for current conditions in your area.

👤 You: bye
🤖 It was great chatting with you!
🤖 Take care and have a wonderful day! 👋
```

## 🔧 Features

- **Natural Conversation**: AI responds like a real person
- **Error Handling**: Gracefully handles API failures, rate limits, timeouts
- **Conversation Memory**: Remembers context from recent messages
- **Keyboard Interrupt**: Ctrl+C to exit gracefully
- **API Key Validation**: Checks key format and provides helpful error messages

## 🛠️ Troubleshooting

### Common Issues:

1. **"Invalid API key"**: Make sure your key starts with `sk-` and is from OpenAI
2. **"Rate limit exceeded"**: You've hit usage limits, wait or upgrade your plan
3. **"Package not found"**: Run `pip install openai`
4. **"Network error"**: Check your internet connection

### Cost Tips:
- GPT-3.5-turbo is very affordable (~$0.002 per 1K tokens)
- Monitor usage in your OpenAI dashboard
- The chatbot limits responses to 200 tokens to keep costs low

## 🎯 Customization

Edit `ai_chatbot.py` to customize:
- **Model**: Change `gpt-3.5-turbo` to `gpt-4`
- **Response length**: Adjust `max_tokens`
- **Creativity**: Change `temperature` (0.0 = consistent, 1.0 = creative)
- **Personality**: Modify the system message
