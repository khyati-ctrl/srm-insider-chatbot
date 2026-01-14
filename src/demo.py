"""
Demo Script - Test the chatbot with predefined questions
Free & Simple - No AI models needed!
"""

import os
from chatbot import SRMInsiderBot


def main():
    """
    Test the chatbot with the 5 required questions.
    """
    
    # Find text or PDF files in the pdfs folder
    pdf_folder = os.path.join(os.path.dirname(__file__), "..", "pdfs")
    
    # Prefer .txt files, then .pdf files
    txt_files = [f for f in os.listdir(pdf_folder) if f.endswith(".txt")]
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    
    if txt_files:
        pdf_path = os.path.join(pdf_folder, txt_files[0])
    elif pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_files[0])
    else:
        print("Error: No text or PDF files found in the 'pdfs' folder.")
        print("Please add a .txt or .pdf file to the 'pdfs' folder first.")
        return
    
    # Initialize chatbot
    print("🤖 Initializing SRM Insider Chatbot...\n")
    bot = SRMInsiderBot(pdf_path)
    
    # Load file
    if not bot.load_pdf():
        return
    
    print()  # Add space
    
    # Test questions
    test_questions = [
        "What is SRM INSIDER?",
        "When did it start?",
        "Who is the founder of SRM INSIDER?",
        "What are the domains of SRM INSIDER?",
        "What is SRM Roomie?"
    ]
    
    print("="*70)
    print("Testing SRM Insider Chatbot with Required Questions")
    print("="*70 + "\n")
    
    for i, question in enumerate(test_questions, 1):
        print(f"Question {i}: {question}")
        result = bot.answer_question(question)
        print(f"Answer: {result['answer']}\n")
        if result["sources"]:
            print(f"Found in sections: {', '.join(str(p) for p in result['sources'])}")
        print("-" * 70 + "\n")


if __name__ == "__main__":
    main()
