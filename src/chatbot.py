"""
SRM Insider AI Chatbot - Main Module
Simple, beginner-friendly PDF question answerer
No AI models, completely free, uses keyword matching
"""

import os
from pathlib import Path
from typing import List, Tuple
from PyPDF2 import PdfReader


class SRMInsiderBot:
    """
    A simple, free chatbot that reads PDF documents and answers questions
    by searching for relevant text. No AI models needed!
    """

    def __init__(self, pdf_path: str = None):
        """
        Initialize the chatbot.
        
        Args:
            pdf_path: Path to the PDF file to load
        """
        self.pdf_path = pdf_path
        self.pdf_text = ""
        self.pages = []  # Store text from each page
        self.page_count = 0

    def load_pdf(self, pdf_path: str = None) -> bool:
        """
        Load and extract text from a PDF file (or .txt file as fallback).
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            True if successful, False otherwise
        """
        path = pdf_path or self.pdf_path
        
        if not path or not os.path.exists(path):
            print(f"Error: File not found at {path}")
            return False
        
        try:
            # If it's a .txt file, load it directly
            if path.endswith('.txt'):
                print(f"Loading text file: {path}")
                with open(path, 'r', encoding='utf-8') as f:
                    self.pdf_text = f.read()
                    self.pages = self.pdf_text.split('\n\n')  # Split by paragraphs
                    self.page_count = len(self.pages)
                print(f"✓ Loaded {self.page_count} sections from text file")
                print(f"✓ Total text length: {len(self.pdf_text)} characters")
                return True
            
            # Otherwise try PDF
            print(f"Loading PDF: {path}")
            reader = PdfReader(path)
            self.page_count = len(reader.pages)
            
            # Extract text from all pages
            self.pages = []
            for page_num, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text.strip():  # Only add non-empty pages
                    self.pages.append(page_text)
                    self.pdf_text += page_text + "\n"
            
            if not self.pdf_text.strip():
                print(f"⚠️  Warning: PDF appears to be image-based or empty")
                print(f"   Loaded {len(reader.pages)} pages but no text extracted")
                print(f"   Try adding a .txt file to the pdfs folder instead")
                return False
            
            print(f"✓ Loaded {self.page_count} pages from PDF")
            print(f"✓ Total text length: {len(self.pdf_text)} characters")
            return True
            
        except Exception as e:
            print(f"Error loading file: {e}")
            return False

    def find_relevant_text(self, question: str, num_results: int = 3) -> List[Tuple[str, int]]:
        """
        Find relevant text from the PDF that matches the question.
        
        Args:
            question: The question to ask
            num_results: Number of relevant passages to return
            
        Returns:
            List of (text, page_number) tuples
        """
        if not self.pdf_text:
            return []
        
        # Get keywords from the question (remove small words)
        keywords = [word.lower() for word in question.split() 
                   if len(word) > 2 and word.lower() not in ['the', 'and', 'for', 'are', 'what', 'who', 'when', 'where', 'why', 'how', 'did', 'was', 'is', 'of', 'in', 'to']]
        
        if not keywords:
            return []
        
        # Search in each page and score them
        results = []
        for page_num, page_text in enumerate(self.pages):
            # Count keyword matches in this page
            score = 0
            for keyword in keywords:
                score += page_text.lower().count(keyword)
            
            if score > 0:
                # Find the most relevant sentence/paragraph
                sentences = page_text.split('.')
                best_sentence = ""
                best_score = 0
                
                for sentence in sentences:
                    sent_score = sum(sentence.lower().count(keyword) for keyword in keywords)
                    if sent_score > best_score:
                        best_score = sent_score
                        best_sentence = sentence.strip()
                
                if best_sentence:
                    results.append((best_sentence, page_num + 1, score))
        
        # Sort by score (relevance) and return top results
        results.sort(key=lambda x: x[2], reverse=True)
        return [(text, page) for text, page, _ in results[:num_results]]

    def answer_question(self, question: str) -> dict:
        """
        Answer a question by searching the PDF content.
        
        Args:
            question: The question to ask
            
        Returns:
            Dictionary with answer and source information
        """
        if not self.pdf_text:
            return {
                "answer": "Error: No PDF loaded. Please load a PDF first.",
                "sources": []
            }
        
        # Find relevant passages
        relevant_texts = self.find_relevant_text(question, num_results=3)
        
        if not relevant_texts:
            return {
                "answer": "I couldn't find relevant information about that in the PDF. Try asking something else!",
                "sources": []
            }
        
        # Build answer from relevant texts
        answer_parts = []
        source_pages = set()
        
        for text, page in relevant_texts:
            answer_parts.append(text)
            source_pages.add(page)
        
        answer = " ".join(answer_parts)
        
        return {
            "answer": answer if answer else "No direct answer found, but these pages might help.",
            "sources": sorted(list(source_pages))
        }

    def interactive_chat(self):
        """
        Start an interactive chat session.
        """
        if not self.pdf_text:
            print("Error: No PDF loaded. Please load a PDF first.")
            return
        
        print("\n" + "="*60)
        print("SRM Insider Chatbot - Interactive Mode")
        print("="*60)
        print("Type 'quit' or 'exit' to end the conversation\n")
        
        while True:
            question = input("You: ").strip()
            
            if question.lower() in ["quit", "exit"]:
                print("Bot: Goodbye! Thank you for using SRM Insider Chatbot.")
                break
            
            if not question:
                continue
            
            result = self.answer_question(question)
            print(f"\nBot: {result['answer']}\n")
            
            if result["sources"]:
                pages_str = ", ".join(str(p) for p in result["sources"])
                print(f"Source pages: {pages_str}")
                print("-" * 60 + "\n")

