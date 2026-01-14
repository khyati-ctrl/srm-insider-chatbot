"""
SRM Insider AI Chatbot - Main Module
Handles PDF processing and Q&A functionality
"""

import os
from pathlib import Path
from typing import List, Optional
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()


class SRMInsiderBot:
    """
    A beginner-friendly chatbot that reads PDF documents and answers questions.
    """

    def __init__(self, pdf_path: str = None):
        """
        Initialize the chatbot.
        
        Args:
            pdf_path: Path to the PDF file to load
        """
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in .env file")
        
        self.pdf_path = pdf_path
        self.vector_store = None
        self.qa_chain = None
        self.documents = []

    def load_pdf(self, pdf_path: str = None) -> bool:
        """
        Load and process a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            True if successful, False otherwise
        """
        path = pdf_path or self.pdf_path
        
        if not path or not os.path.exists(path):
            print(f"Error: PDF file not found at {path}")
            return False
        
        try:
            print(f"Loading PDF: {path}")
            loader = PyPDFLoader(path)
            self.documents = loader.load()
            print(f"✓ Loaded {len(self.documents)} pages from PDF")
            return True
        except Exception as e:
            print(f"Error loading PDF: {e}")
            return False

    def process_documents(self) -> bool:
        """
        Process documents into chunks and create embeddings.
        
        Returns:
            True if successful, False otherwise
        """
        if not self.documents:
            print("Error: No documents loaded. Please load a PDF first.")
            return False
        
        try:
            print("Processing documents...")
            
            # Split documents into chunks
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50,
                separators=["\n\n", "\n", " ", ""]
            )
            chunks = splitter.split_documents(self.documents)
            print(f"✓ Created {len(chunks)} text chunks")
            
            # Create embeddings and vector store
            print("Creating embeddings and vector store...")
            embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)
            self.vector_store = FAISS.from_documents(chunks, embeddings)
            print("✓ Vector store created successfully")
            
            # Create QA chain
            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo",
                temperature=0.5,
                openai_api_key=self.api_key
            )
            
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=self.vector_store.as_retriever(search_kwargs={"k": 3}),
                return_source_documents=True
            )
            print("✓ Q&A chain initialized")
            return True
            
        except Exception as e:
            print(f"Error processing documents: {e}")
            return False

    def answer_question(self, question: str) -> dict:
        """
        Answer a question based on the PDF content.
        
        Args:
            question: The question to ask
            
        Returns:
            Dictionary with answer and source information
        """
        if not self.qa_chain:
            return {
                "answer": "Error: Chatbot not initialized. Please load a PDF first.",
                "sources": []
            }
        
        try:
            result = self.qa_chain({"query": question})
            return {
                "answer": result.get("result", "No answer found"),
                "sources": result.get("source_documents", [])
            }
        except Exception as e:
            return {
                "answer": f"Error answering question: {e}",
                "sources": []
            }

    def interactive_chat(self):
        """
        Start an interactive chat session.
        """
        if not self.qa_chain:
            print("Error: Chatbot not initialized. Please load a PDF first.")
            return
        
        print("\n" + "="*60)
        print("SRM Insider AI Bot - Interactive Mode")
        print("="*60)
        print("Type 'quit' or 'exit' to end the conversation\n")
        
        while True:
            question = input("You: ").strip()
            
            if question.lower() in ["quit", "exit"]:
                print("Bot: Goodbye! Thank you for using SRM Insider AI Bot.")
                break
            
            if not question:
                continue
            
            result = self.answer_question(question)
            print(f"\nBot: {result['answer']}\n")
            
            if result["sources"]:
                print(f"Sources: Page(s) {', '.join(set(str(doc.metadata.get('page', 'Unknown')) for doc in result['sources']))}")
                print("-" * 60 + "\n")
