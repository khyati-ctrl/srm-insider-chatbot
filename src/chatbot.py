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

    def find_relevant_text(self, question: str, num_results: int = 1) -> List[Tuple[str, int]]:
        """
        Find relevant text from the PDF that matches the question.
        
        Args:
            question: The question to ask
            num_results: Number of relevant passages to return (default: 1 for concise answers)
            
        Returns:
            List of (text, page_number) tuples
        """
        if not self.pdf_text:
            return []
        
        # Clean up the question first
        question_clean = question.lower().rstrip('?').strip()
        question_clean = ''.join(c for c in question_clean if c.isalnum() or c.isspace())
        
        # Get keywords from the question (remove small words)
        stop_words = {'the', 'and', 'for', 'are', 'what', 'who', 'when', 'where', 'why', 'how', 'did', 'was', 'is', 'of', 'in', 'to', 'a', 'an', 'be', 'by', 'do', 'it', 'or', 'as'}
        keywords = [word.lower() for word in question_clean.split() 
                   if len(word) > 2 and word.lower() not in stop_words]
        
        if not keywords:
            return []
        
        # Search in each section and score them
        results = []
        for page_num, page_text in enumerate(self.pages):
            if not page_text.strip():
                continue
            
            # Clean up the section text
            clean_text = " ".join(page_text.split())
            page_lower = clean_text.lower()
            
            score = 0
            
            # Extract the section header (first line before any period/question mark)
            section_header = clean_text.split('?')[0] if '?' in clean_text else clean_text.split('.')[0]
            section_header = section_header.strip().lower()
            # Remove special characters from header for matching
            section_header_clean = ''.join(c for c in section_header if c.isalnum() or c.isspace())
            
            # Strategy 1: Check if user question and section header have similar patterns
            # by comparing cleaned versions
            if section_header_clean == question_clean:
                # Perfect match - extremely high score!
                score += 1000
            else:
                # Count how many keywords from user question appear in the section header
                header_keyword_matches = sum(1 for kw in keywords if kw in section_header_clean)
                
                if header_keyword_matches >= len(keywords) - 1:  # Allow max 1 mismatch
                    # Very high score if most keywords match in header
                    score += 100 + (header_keyword_matches * 50)
                elif header_keyword_matches > 0:
                    # Still good score for partial header match
                    score += 30 * header_keyword_matches
                
                # Strategy 2: Body keyword matching (less important than header)
                for keyword in keywords:
                    body_occurrences = page_lower.count(keyword)
                    # Only count first few occurrences to avoid bias towards longer passages
                    score += min(body_occurrences, 2) * 1
            
            if score > 0:
                # Use the whole section if it's reasonably sized
                if len(clean_text) < 1000:
                    results.append((clean_text, page_num + 1, score))
                else:
                    # For longer sections, find the most relevant sentence
                    sentences = clean_text.split('.')
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
        if results:
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
        
        # Find relevant passages (only 1 for concise answers)
        relevant_texts = self.find_relevant_text(question, num_results=1)
        
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

