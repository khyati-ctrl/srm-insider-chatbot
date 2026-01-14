"""
Demo Script - Test the chatbot with predefined questions
"""

import os
from chatbot import SRMInsiderBot


def main():
    """
    Test the chatbot with the 5 required questions.
    """
    
    # Find PDF in the pdfs folder
    pdf_folder = os.path.join(os.path.dirname(__file__), "..", "pdfs")
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    
    if not pdf_files:
        print("Error: No PDF files found in the 'pdfs' folder.")
        print("Please add your SRM Insider PDF to the 'pdfs' folder first.")
        return
    
    pdf_path = os.path.join(pdf_folder, pdf_files[0])
    
    # Initialize chatbot
    print("🤖 Initializing SRM Insider AI Bot...\n")
    bot = SRMInsiderBot(pdf_path)
    
    # Load PDF
    if not bot.load_pdf():
        return
    
    # Process documents
    if not bot.process_documents():
        return
    
    # Test questions
    test_questions = [
        "What is SRM INSIDER?",
        "When did it start?",
        "Who is the founder of SRM INSIDER?",
        "What are the domains of SRM INSIDER?",
        "What is SRM Roomie?"
    ]
    
    print("\n" + "="*70)
    print("Testing SRM Insider AI Bot with Required Questions")
    print("="*70 + "\n")
    
    for i, question in enumerate(test_questions, 1):
        print(f"Question {i}: {question}")
        result = bot.answer_question(question)
        print(f"Answer: {result['answer']}\n")
        print("-" * 70 + "\n")


if __name__ == "__main__":
    main()
