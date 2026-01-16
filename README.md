# SRM Insider Chatbot

A simple, free, and beginner-friendly Python chatbot that reads PDF or text documents and answers questions using keyword matching. No AI models needed, completely free to use!

## 🚀 Features

- **PDF & Text Support**: Reads both PDF files and plain text files
- **Keyword-Based Matching**: Uses intelligent keyword matching to find relevant answers (no AI API calls needed)
- **Interactive Chat**: Real-time conversation mode with source tracking
- **Fast & Free**: No API keys required, runs entirely on your computer
- **Simple Architecture**: Clean, easy-to-understand code with clear explanations
- **Multiple Input Modes**: Interactive mode, demo mode, or test mode

## 📋 Project Structure

```
srm-insider-chatbot/
├── src/
│   ├── chatbot.py              # Main chatbot class (SRMInsiderBot)
│   ├── main.py                 # Interactive entry point
│   ├── demo.py                 # Automated demo with test questions
│   ├── demo_text_chatbot.py    # Text file demo
│   ├── test_interactive.py     # Interactive testing mode
│   ├── pdf_to_text_converter.py # Convert PDF to text utility
│   ├── create_sample_pdf.py    # Generate sample PDF for testing
│   └── __pycache__/            # Python cache folder
├── pdfs/                       # PDF/text file storage folder
│   └── SRM_Content.txt         # Sample SRM Insider content
├── docs/                       # Documentation folder
├── requirements.txt            # Python dependencies
├── setup_git.sh               # Git setup script
├── QUICKSTART.md              # Quick start guide
└── README.md                  # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- No API keys or internet connection needed!

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd srm-insider-chatbot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your content**
   - Place your SRM Insider PDF or TXT file in the `pdfs/` folder
   - The chatbot will automatically detect and use it

## 💻 Usage

### Interactive Mode
Start a conversation with the chatbot:
```bash
cd src
python main.py
```
Then type your questions. Type `quit` or `exit` to end the conversation.

### Run Demo with Test Questions
Test the chatbot with 5 predefined questions:
```bash
cd src
python demo.py
```

### Interactive Text Demo
Test with more sample questions:
```bash
cd src
python demo_text_chatbot.py
```

### Interactive Testing Mode
Another interactive mode for testing:
```bash
cd src
python test_interactive.py
```

## 📊 How It Works

The chatbot uses a **keyword matching algorithm**:

```
1. User asks a question
   ↓
2. Extract keywords from the question
   (remove small words like "the", "and", "what")
   ↓
3. Search through PDF/text content
   for sections containing those keywords
   ↓
4. Score each section based on:
   - Keyword matches in section headers (highest score)
   - Keyword matches in body text (lower score)
   - Exact phrase matching
   ↓
5. Return the highest-scoring section as the answer
   along with source page number
   ↓
6. Display answer to user
```

## 🔧 Core Components

### 1. **chatbot.py** - Main Chatbot Engine
The `SRMInsiderBot` class handles everything:

- `__init__()`: Initialize the chatbot with a PDF/text file path
- `load_pdf()`: Load and extract text from PDF or TXT files
- `find_relevant_text()`: Search for text matching user's question
- `answer_question()`: Generate an answer with source information
- `interactive_chat()`: Run an interactive conversation

**Key Features:**
- Supports both PDF and TXT files
- Splits content into pages/sections
- Scores sections by relevance
- Returns top matching result with page number

### 2. **main.py** - Interactive Entry Point
Starts the chatbot in interactive mode:
- Finds available PDF/TXT files in the `pdfs/` folder
- Lets user choose which file to load (if multiple exist)
- Starts interactive chat session

### 3. **demo.py** - Automated Testing
Tests chatbot with 5 required questions:
1. What is SRM INSIDER?
2. When did it start?
3. Who is the founder of SRM INSIDER?
4. What are the domains of SRM INSIDER?
5. What is SRM Roomie?

### 4. **demo_text_chatbot.py** - Text Demo
Demonstrates chatbot with 7 sample questions about SRM Insider.

### 5. **test_interactive.py** - Interactive Test Mode
Another interactive mode for testing the chatbot.

### 6. **pdf_to_text_converter.py** - Utility Tool
Converts PDF files to plain text for easier processing.

### 7. **create_sample_pdf.py** - Sample Generator
Creates a sample PDF with SRM Insider information for testing.

## 📝 How the Algorithm Works

### Keyword Extraction
```python
# Question: "What is SRM Insider?"
# Extracted keywords: ["srm", "insider"]
# (removed: "what", "is")
```

### Scoring System
- **Perfect header match**: 1000 points
- **Most keywords in header**: 100-150 points
- **Some keywords in header**: 30-50 points
- **Keywords in body text**: 1-2 points each

### Result Selection
- Scores all content sections
- Returns section with highest score
- If no match found, says "couldn't find relevant information"

## 🎯 Example Usage

```bash
$ python main.py
==============================================================
Welcome to SRM Insider Chatbot
(Free & Simple - No AI Models!)
==============================================================

Loading text file: ../pdfs/SRM_Content.txt
✓ Loaded 5 sections from text file
✓ Total text length: 2500 characters

============================================================
SRM Insider Chatbot - Interactive Mode
============================================================
Type 'quit' or 'exit' to end the conversation

You: What is SRM Insider?
Bot: SRM Insider is a premier community platform...
Source pages: 1

You: Who founded it?
Bot: SRM Insider was founded by a group of visionary students...
Source pages: 1

You: quit
Bot: Goodbye! Thank you for using SRM Insider Chatbot.
```

## 🔑 Key Technologies

- **PyPDF2**: PDF text extraction
- **Python 3.8+**: Programming language
- **Standard Library**: File I/O, string processing

## ✨ Why This Chatbot is Special

1. **Free Forever**: No API costs, no subscriptions
2. **No Internet Needed**: Works completely offline
3. **Privacy**: Your data never leaves your computer
4. **Simple**: Easy to understand and modify
5. **Fast**: Instant responses without waiting for AI
6. **Beginner-Friendly**: Well-commented code with clear logic

## 📖 Code Explanation

Each line of code has been written with simplicity in mind:
- Clear variable names
- Detailed comments
- Logical structure
- Type hints for clarity

For a detailed line-by-line explanation of the code, see the documentation or ask for specific file explanations.

## 🚀 Getting Started

1. Place your PDF or TXT file in the `pdfs/` folder
2. Run `python main.py` from the `src/` folder
3. Start asking questions!
4. Type `quit` to exit

## 📞 Support

For issues or questions:
1. Check the QUICKSTART.md file
2. Review the code comments in the src/ folder
3. Test with the demo.py file first

## 📄 License

This project is open source and free to use!
