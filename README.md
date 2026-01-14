# SRM Insider AI Bot

A beginner-friendly Python chatbot that reads PDF documents and answers questions about their content. Built specifically for the SRM Insider project.

## 🚀 Features

- **PDF Reading**: Automatically extracts and processes PDF documents
- **Intelligent Q&A**: Uses OpenAI's GPT models to answer questions based on PDF content
- **Vector Embeddings**: Utilizes FAISS for efficient document retrieval
- **Interactive Chat**: Real-time conversation mode with source tracking
- **Beginner-Friendly**: Clean, well-documented code with clear architecture

## 📋 Project Structure

```
srm-insider-chatbot/
├── src/
│   ├── chatbot.py          # Main chatbot class
│   ├── main.py             # Interactive entry point
│   └── demo.py             # Demo with test questions
├── pdfs/                   # PDF storage folder
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))

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

4. **Set up environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   # OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
   ```

5. **Add your PDF**
   - Place your SRM Insider PDF in the `pdfs/` folder
   - Filename can be anything ending in `.pdf`

## 💻 Usage

### Interactive Mode
```bash
cd src
python main.py
```

Then type your questions about the PDF content. Type `quit` or `exit` to end.

### Run Demo with Test Cases
```bash
cd src
python demo.py
```

This will test the chatbot with the 5 required questions:
1. What is SRM INSIDER?
2. When did it start?
3. Who is the founder of SRM INSIDER?
4. What are the domains of SRM INSIDER?
5. What is SRM Roomie?

## 📊 How It Works

```
PDF File
   ↓
[Load PDF] → PyPDFLoader reads document
   ↓
[Split Text] → RecursiveCharacterTextSplitter chunks document
   ↓
[Create Embeddings] → OpenAIEmbeddings converts chunks to vectors
   ↓
[Store Vectors] → FAISS stores embeddings for fast retrieval
   ↓
[User Question] → Input is converted to embedding
   ↓
[Retrieve Context] → FAISS finds most relevant chunks
   ↓
[Generate Answer] → GPT-3.5-turbo generates response using context
   ↓
[Return Answer] → Display result with source information
```

## 🔧 Code Structure

### `chatbot.py` - Main Class
The `SRMInsiderBot` class handles:
- **`__init__`**: Initialize with API key and PDF path
- **`load_pdf()`**: Load PDF file using PyPDFLoader
- **`process_documents()`**: Split documents, create embeddings, and initialize Q&A chain
- **`answer_question()`**: Answer a single question
- **`interactive_chat()`**: Start interactive conversation mode

### `main.py` - Entry Point
- User-friendly interface
- PDF selection (if multiple files exist)
- Launches interactive chat mode

### `demo.py` - Testing
- Loads first PDF automatically
- Tests 5 required questions
- Displays answers with source page numbers

## 📝 Dependencies

| Package | Purpose |
|---------|---------|
| `langchain` | LLM orchestration framework |
| `openai` | OpenAI API client |
| `python-dotenv` | Environment variable management |
| `PyPDF2` | PDF reading |
| `faiss-cpu` | Vector similarity search |

## ⚠️ Important Notes

- **API Costs**: Using this chatbot will consume OpenAI API credits. Monitor your usage on the [OpenAI dashboard](https://platform.openai.com/account/billing/overview).
- **API Key Security**: Never commit your `.env` file to Git. It's already in `.gitignore`.
- **PDF Quality**: Works best with text-based PDFs. Scanned images may not work well.

## 🎯 Test Cases

The chatbot is designed to answer these 5 specific questions:

1. **"What is SRM INSIDER?"** - Should explain the organization
2. **"When did it start?"** - Should provide founding date
3. **"Who is the founder of SRM INSIDER?"** - Should identify founder(s)
4. **"What are the domains of SRM INSIDER?"** - Should list domains/areas
5. **"What is SRM Roomie?"** - Should explain SRM Roomie service/product

## 🐛 Troubleshooting

### "OPENAI_API_KEY not found"
- Ensure `.env` file exists in the project root
- Verify OPENAI_API_KEY is set correctly
- Check there are no extra spaces in the key

### "No PDF files found"
- Create a `pdfs/` folder if it doesn't exist
- Add your PDF file to the folder
- Ensure file has `.pdf` extension

### "ModuleNotFoundError"
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

## 📈 Performance Tips

- **Chunk Size**: Adjust in `chatbot.py` (default: 500 characters)
- **Retrieval Count**: Change `search_kwargs={"k": 3}` to retrieve more/fewer context chunks
- **Temperature**: Adjust in `ChatOpenAI()` for more/less creative responses
  - Lower (0.0-0.3): More factual and consistent
  - Higher (0.7-1.0): More creative and varied

## 🚀 Future Enhancements

- [ ] Support for multiple PDFs
- [ ] Document caching to reduce API calls
- [ ] Web interface with Streamlit
- [ ] Chat history logging
- [ ] Support for other LLM providers (Hugging Face, Cohere, etc.)
- [ ] Streaming responses for faster user experience

## 📜 License

This project is created for the SRM Insider AI Bot task.

## ❓ Need Help?

Refer to the documentation in the `docs/` folder for:
- Architecture flowchart
- API integration guide
- FAQ

---

**Deadline**: January 18, 2026

**Built with ❤️ using LangChain and OpenAI**
The bot reads a PDF document containing information about SRM Insider and answers user questions based only on that document.

## Features
- Reads and processes a PDF file
- Searches relevant content from the document
- Answers questions using AI
- Command-line interface

## Tech Stack
- Python
- PyPDF2
- Sentence Transformers
- FAISS
- HuggingFace Transformers

## How It Works
PDF → Text Extraction → Text Chunking → Vector Search → AI Answer

## How to Run
Instructions will be added after setup.
