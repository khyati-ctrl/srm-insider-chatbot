#!/usr/bin/env python3
"""
Simple interactive test of the chatbot with improved conciseness
"""

import os
from chatbot import SRMInsiderBot


def test_interactive():
    """
    Interactive chat with improved concise responses.
    """
    print("="*60)
    print("SRM Insider Chatbot - Interactive Mode")
    print("(Now with concise, specific answers!)")
    print("="*60 + "\n")
    
    # Use the text file
    pdfs_folder = os.path.join(os.path.dirname(__file__), "..", "pdfs")
    text_file = os.path.join(pdfs_folder, "SRM_Content.txt")
    
    if not os.path.exists(text_file):
        print(f"ERROR: Text file not found: {text_file}")
        return
    
    print(f"Loading content from: SRM_Content.txt\n")
    
    # Initialize and load chatbot
    bot = SRMInsiderBot(text_file)
    if not bot.load_pdf():
        return
    
    print()
    print("Ask me about SRM Insider or SRM Roomie!")
    print("Type 'quit' or 'exit' to end the chat\n")
    print("="*60 + "\n")
    
    # Interactive chat loop
    while True:
        question = input("You: ").strip()
        
        if not question:
            continue
        
        if question.lower() in ["quit", "exit"]:
            print("Bot: Goodbye!")
            break
        
        result = bot.answer_question(question)
        
        # Print answer
        print(f"\nBot: {result['answer']}\n")
        
        # Print source if available
        if result['sources']:
            sources_str = ", ".join(str(s) for s in result['sources'])
            print(f"[Source: page {sources_str}]")
        
        print()


if __name__ == "__main__":
    test_interactive()
