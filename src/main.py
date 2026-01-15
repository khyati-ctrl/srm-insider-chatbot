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
    
    # Find PDF and text files
    pdf_folder = os.path.join(os.path.dirname(__file__), "..", "pdfs")
    
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
        print(f"📁 Created 'pdfs' folder at: {pdf_folder}")
        print("Please add your SRM Insider PDF or TXT file there.\n")
        return
    
    # Look for both PDF and TXT files
    all_files = [f for f in os.listdir(pdf_folder) if f.endswith((".pdf", ".txt"))]
    
    if not all_files:
        print("❌ No PDF or TXT files found in the 'pdfs' folder.")
        print(f"Please add your SRM Insider PDF or TXT file to: {pdf_folder}\n")
        return
    
    # Select file
    if len(all_files) > 1:
        print("Available files:")
        for i, file in enumerate(all_files, 1):
            print(f"  {i}. {file}")
        choice = input("\nSelect file (enter number): ").strip()
        try:
            file_path = os.path.join(pdf_folder, all_files[int(choice) - 1])
        except (ValueError, IndexError):
            print("Invalid selection")
            return
    else:
        file_path = os.path.join(pdf_folder, all_files[0])
    
    # Initialize chatbot
    print(f"\n🤖 Initializing chatbot with: {os.path.basename(file_path)}\n")
    
    try:
        bot = SRMInsiderBot(file_path)
        
        # Load file (PDF or TXT)
        if not bot.load_pdf():
            return
        
        print()  # Add space
        
        # Start interactive chat
        bot.interactive_chat()
        
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
