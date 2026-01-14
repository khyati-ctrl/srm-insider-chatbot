# Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set API Key
Create `.env` file in the project root:
```
OPENAI_API_KEY=sk-your-key-here
```

Get your free key from: https://platform.openai.com/api-keys

### 3. Add Your PDF
Place the SRM Insider PDF in the `pdfs/` folder.

### 4. Run the Demo
```bash
cd src
python demo.py
```

You should see answers to all 5 test questions!

## 📁 Project Files

### Source Code (`src/`)
- **chatbot.py** - Main `SRMInsiderBot` class (120 lines)
- **main.py** - Interactive chat interface (80 lines)
- **demo.py** - Test script for 5 questions (50 lines)
- **create_sample_pdf.py** - Helper to create test PDFs

### Documentation (`docs/`)
- **ARCHITECTURE.md** - System design & data flow
- **SETUP_GUIDE.md** - Detailed installation steps
- **GITHUB_SETUP.md** - GitHub repository guide

### Configuration
- **requirements.txt** - Python dependencies
- **.env.example** - Environment template
- **.gitignore** - Git ignore patterns
- **README.md** - Main documentation

### Data (`pdfs/`)
- Place your PDF here
- Any `.pdf` file will be automatically loaded

## 💡 Key Features

✅ **Reads PDFs** - Automatically extracts text from documents
✅ **Answers Questions** - Uses GPT-3.5-turbo with document context
✅ **Vector Search** - FAISS for fast, accurate retrieval
✅ **Shows Sources** - Displays which PDF pages were used
✅ **Beginner-Friendly** - Clean code with clear comments
✅ **Interactive Mode** - Chat with the bot in real-time
✅ **Demo Mode** - Automatically test 5 required questions

## 🎯 Test It With

### Interactive Mode
```bash
cd src
python main.py
```
Then ask any question about the PDF!

### Demo Mode
```bash
cd src
python demo.py
```
Automatically tests:
1. What is SRM INSIDER?
2. When did it start?
3. Who is the founder of SRM INSIDER?
4. What are the domains of SRM INSIDER?
5. What is SRM Roomie?

## 🐛 Common Issues

| Issue | Solution |
|-------|----------|
| API key not found | Create `.env` with your OpenAI key |
| No PDF found | Add PDF to `pdfs/` folder |
| Modules not installed | Run `pip install -r requirements.txt` |
| Permission denied | Check file permissions or move folder |

## 📊 Project Structure

```
srm-insider-chatbot/
├── src/
│   ├── chatbot.py              # Main class
│   ├── main.py                 # Interactive mode
│   ├── demo.py                 # Test harness
│   └── create_sample_pdf.py    # PDF generator
├── pdfs/                       # Put PDF here
├── docs/
│   ├── ARCHITECTURE.md         # How it works
│   ├── SETUP_GUIDE.md          # Step-by-step setup
│   └── GITHUB_SETUP.md         # Git instructions
├── requirements.txt            # Dependencies
├── .env.example                # Config template
└── README.md                   # Full documentation
```

## 🔐 Important

- ⚠️ Never commit `.env` file (contains API key!)
- ⚠️ `.env` is in `.gitignore` - safe to use
- ⚠️ API costs money - monitor at https://platform.openai.com/account/billing/overview

## 📝 Git Commits

Your project has meaningful commits:

```
1. Initial commit - Project structure
2. Add: Core chatbot - Main functionality
3. Add: Demo script - Test harness
4. Add: Documentation - Complete guides
5. Add: PDF generator - Testing tools
```

## 🎬 For the Demo Video

Record this:
1. Open terminal in project folder
2. Run `python src/demo.py`
3. Show each question and answer
4. Show the source PDF page numbers
5. Total time: ~2-3 minutes

## 📤 For GitHub Submission

```bash
git remote add origin https://github.com/YOUR_USERNAME/srm-insider-chatbot.git
git branch -M main
git push -u origin main
```

Then submit:
1. GitHub URL
2. Demo video (max 5 mins)
3. Reference ARCHITECTURE.md for flowchart

## ✨ What's Included

- ✅ PDF reading and processing
- ✅ Intelligent Q&A with context
- ✅ Vector embeddings (FAISS)
- ✅ Interactive chat interface
- ✅ Test script for 5 questions
- ✅ Complete documentation
- ✅ Example PDF generator
- ✅ Good commit history
- ✅ Beginner-friendly code

## 🚀 Next Steps

1. [ ] Get OpenAI API key (free trial available)
2. [ ] Create `.env` file with your key
3. [ ] Run `pip install -r requirements.txt`
4. [ ] Add your PDF to `pdfs/` folder
5. [ ] Run `python src/demo.py`
6. [ ] Test interactive mode: `python src/main.py`
7. [ ] Record demo video
8. [ ] Push to GitHub
9. [ ] Submit project!

---

**Questions?** Check the detailed guides in the `docs/` folder!

**Deadline**: January 18, 2026 ⏰
