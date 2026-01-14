"""
Interactive main entry point for the chatbot
Simple, free, no AI models - just keyword matching!
"""

import os
import sys
from chatbot import SRMInsiderBot


def main():
    """
    Main entry point for the chatbot application.
    """
    
    print("="*60)
    print("Welcome to SRM Insider Chatbot")
    print("(Free & Simple - No AI Models!)")
    print("="*60 + "\n")
    
    # Find PDF files
    pdf_folder = os.path.join(os.path.dirname(__file__), "..", "pdfs")
    
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
        print(f"📁 Created 'pdfs' folder at: {pdf_folder}")
        print("Please add your SRM Insider PDF file there.\n")
        return
    
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
    
    if not pdf_files:
        print("❌ No PDF files found in the 'pdfs' folder.")
        print(f"Please add your SRM Insider PDF to: {pdf_folder}\n")
        return
    
    # Select PDF
    if len(pdf_files) > 1:
        print("Available PDFs:")
        for i, pdf in enumerate(pdf_files, 1):
            print(f"  {i}. {pdf}")
        choice = input("\nSelect PDF (enter number): ").strip()
        try:
            pdf_path = os.path.join(pdf_folder, pdf_files[int(choice) - 1])
        except (ValueError, IndexError):
            print("Invalid selection")
            return
    else:
        pdf_path = os.path.join(pdf_folder, pdf_files[0])
    
    # Initialize chatbot
    print(f"\n🤖 Initializing chatbot with: {os.path.basename(pdf_path)}\n")
    
    try:
        bot = SRMInsiderBot(pdf_path)
        
        # Load PDF
        if not bot.load_pdf():
            return
        
        print()  # Add space
        
        # Start interactive chat
        bot.interactive_chat()
        
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
