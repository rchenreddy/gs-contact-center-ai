#!/usr/bin/env python3
"""
Simple script to test if your OpenAI API key works
"""

import os
from openai import OpenAI

def test_api_key():
    """Test if the OpenAI API key is working"""
    
    # Get API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        api_key = input("Enter your OpenAI API key: ").strip()
    
    if not api_key:
        print("❌ No API key provided")
        return False
    
    # Check if it looks like a real key
    if not api_key.startswith('sk-'):
        print("❌ API key should start with 'sk-'")
        return False
    
    if len(api_key) < 20:
        print("❌ API key seems too short")
        return False
    
    print(f"✅ API key format looks correct: {api_key[:10]}...")
    
    try:
        # Test the API
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hello, API key is working!'"}],
            max_tokens=10
        )
        
        print("✅ API key is working!")
        print(f"🤖 Response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing OpenAI API Key...")
    test_api_key()
