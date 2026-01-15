#!/usr/bin/env python3
"""
PDF to Text Converter
Converts PDF files to plain text files for easier processing
"""

import os
from pathlib import Path
from PyPDF2 import PdfReader


def convert_pdf_to_text(pdf_path: str, output_path: str = None) -> bool:
    """
    Convert a PDF file to a plain text file.
    
    Args:
        pdf_path: Path to the PDF file
        output_path: Path where the text file will be saved (optional)
        
    Returns:
        True if successful, False otherwise
    """
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return False
    
    if not pdf_path.endswith('.pdf'):
        print("Error: File must be a PDF file")
        return False
    
    try:
        # Determine output path
        if output_path is None:
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            output_path = os.path.join(os.path.dirname(pdf_path), f"{base_name}.txt")
        
        print(f"Converting PDF: {pdf_path}")
        
        # Read PDF
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        
        extracted_text = ""
        for page_num, page in enumerate(reader.pages, 1):
            page_text = page.extract_text()
            extracted_text += page_text + "\n\n"
            print(f"  Processing page {page_num}/{total_pages}...", end='\r')
        
        # Check if text was extracted
        if not extracted_text.strip():
            print(f"\n⚠️  Warning: No text found in PDF")
            print(f"   The PDF may be image-based or scanned documents")
            return False
        
        # Save to text file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        
        file_size = os.path.getsize(output_path)
        print(f"\n✓ Successfully converted PDF to text")
        print(f"  Total pages: {total_pages}")
        print(f"  Output file: {output_path}")
        print(f"  File size: {file_size} bytes")
        return True
        
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return False


def main():
    """
    Main entry point for PDF conversion.
    Converts all PDF files in the pdfs folder to text files.
    """
    print("="*60)
    print("PDF to Text Converter")
    print("="*60 + "\n")
    
    # Get pdfs folder
    pdfs_folder = os.path.join(os.path.dirname(__file__), "..", "pdfs")
    
    if not os.path.exists(pdfs_folder):
        print(f"❌ PDFs folder not found: {pdfs_folder}")
        return
    
    # Find PDF files
    pdf_files = [f for f in os.listdir(pdfs_folder) if f.endswith(".pdf")]
    
    if not pdf_files:
        print(f"No PDF files found in {pdfs_folder}")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s):\n")
    
    # Convert each PDF
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdfs_folder, pdf_file)
        convert_pdf_to_text(pdf_path)
        print()


if __name__ == "__main__":
    main()
