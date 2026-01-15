#!/usr/bin/env python3
"""
Demo script showing the chatbot answering questions from the text file
"""

import os
from chatbot import SRMInsiderBot


def demo():
    """
    Demonstrate the chatbot with predefined questions.
    """
    print("="*60)
    print("SRM Insider Chatbot - Text File Demo")
    print("="*60 + "\n")
    
    # Use the text file
    pdfs_folder = os.path.join(os.path.dirname(__file__), "..", "pdfs")
    text_file = os.path.join(pdfs_folder, "SRM_Content.txt")
    
    if not os.path.exists(text_file):
        print(f"ERROR: Text file not found: {text_file}")
        return
    
    print(f"[*] Loading content from: SRM_Content.txt\n")
    
    # Initialize and load chatbot
    bot = SRMInsiderBot(text_file)
    if not bot.load_pdf():  # This works for both PDF and TXT
        return
    
    print()
    
    # Sample questions to ask
    questions = [
        "What is SRM Insider?",
        "When was SRM Insider founded?",
        "Who founded SRM Insider?",
        "What are the domains of SRM Insider?",
        "What is SRM Roomie?",
        "What does SRM Insider focus on?",
        "What services does SRM Insider provide?"
    ]
    
    print("Asking the chatbot some questions...\n")
    print("="*60 + "\n")
    
    for question in questions:
        print(f"Q: {question}")
        result = bot.answer_question(question)
        print(f"A: {result['answer']}")
        if result['sources']:
            sources_str = ", ".join(str(s) for s in result['sources'])
            print(f"   [Source: page {sources_str}]")
        print()


if __name__ == "__main__":
    demo()
