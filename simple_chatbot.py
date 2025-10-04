#!/usr/bin/env python3
"""
Simple Chatbot for Training Purposes
====================================

A basic chatbot that demonstrates conversation flow and user interaction.
This script runs in the terminal and follows a structured conversation pattern.
"""

def main():
    """
    Main function that runs the chatbot conversation.
    """
    print("=" * 50)
    print("🤖 Welcome to the Simple Training Chatbot!")
    print("=" * 50)
    
    # Step 1: Greet user and get their name
    print("\nHello! I'm here to help you with banking services.")
    user_name = input("What's your name? ").strip()
    
    # Handle empty name input
    if not user_name:
        user_name = "there"
    
    print(f"\nNice to meet you, {user_name}!")
    
    # Step 2: Ask what they need help with
    print("\nHow can I assist you today?")
    print("Please type either 'account' or 'loan' to continue:")
    
    user_choice = input("Your choice: ").strip().lower()
    
    # Step 3: Process the user's choice and provide appropriate response
    if user_choice == "account":
        handle_account_inquiry(user_name)
    elif user_choice == "loan":
        handle_loan_inquiry(user_name)
    else:
        handle_invalid_choice(user_name)
    
    # Step 4: End conversation politely
    print(f"\nThank you for using our service, {user_name}!")
    print("Have a great day! 👋")
    print("=" * 50)

def handle_account_inquiry(name):
    """
    Handle account-related inquiries.
    
    Args:
        name (str): The user's name for personalization
    """
    print(f"\n📊 Account Services for {name}")
    print("-" * 30)
    print("I can help you with:")
    print("• Checking your account balance")
    print("• Viewing recent transactions")
    print("• Updating your personal information")
    print("• Resolving login issues")
    print("\nWould you like to contact our account specialist for detailed assistance?")

def handle_loan_inquiry(name):
    """
    Handle loan-related inquiries.
    
    Args:
        name (str): The user's name for personalization
    """
    print(f"\n💰 Loan Services for {name}")
    print("-" * 30)
    print("We offer various loan options:")
    print("• Personal loans (starting from 5.99% APR)")
    print("• Home loans (competitive rates available)")
    print("• Business loans (tailored solutions)")
    print("\nOur loan specialists can help you find the best option for your needs.")

def handle_invalid_choice(name):
    """
    Handle invalid user input.
    
    Args:
        name (str): The user's name for personalization
    """
    print(f"\n❌ Sorry {name}, I can only help with 'account' or 'loan' services.")
    print("Please restart the program if you'd like to try again.")

if __name__ == "__main__":
    # Run the chatbot when the script is executed directly
    main()

