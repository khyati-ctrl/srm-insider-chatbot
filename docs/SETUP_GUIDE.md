# Setup & Installation Guide

## Step-by-Step Setup

### Step 1: Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to [API Keys](https://platform.openai.com/account/api-keys)
4. Click "Create new secret key"
5. Copy the key (you won't be able to see it again)

### Step 2: Clone/Download Repository

```bash
# Clone the repository
git clone <your-repo-url>
cd srm-insider-chatbot
```

### Step 3: Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt after activation.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- LangChain (LLM framework)
- OpenAI (API client)
- PyPDF2 (PDF reading)
- FAISS (vector database)
- python-dotenv (environment variables)

### Step 5: Configure API Key

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env  # macOS/Linux
   # OR
   copy .env.example .env  # Windows
   ```

2. Open `.env` in a text editor and add your key:
   ```
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

3. Save the file

### Step 6: Add PDF File

1. Place your SRM Insider PDF in the `pdfs/` folder
2. Any filename ending in `.pdf` works

### Step 7: Test Installation

```bash
cd src
python demo.py
```

If successful, you should see:
```
🤖 Initializing SRM Insider AI Bot...
Loading PDF: ...
✓ Loaded 10 pages from PDF
Processing documents...
✓ Created X text chunks
✓ Vector store created successfully
✓ Q&A chain initialized
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'langchain'"

**Solution**: Reinstall requirements in virtual environment
```bash
# Make sure venv is activated
pip install -r requirements.txt
```

### Issue: "OPENAI_API_KEY not found in environment variables"

**Solution**: 
1. Check `.env` file exists in project root (same level as `src/`, `pdfs/`, etc.)
2. Verify the key is set: `OPENAI_API_KEY=sk-...`
3. No spaces before/after the `=` sign
4. On Windows, restart any open terminals after creating `.env`

### Issue: "No module named 'dotenv'"

**Solution**: Install python-dotenv
```bash
pip install python-dotenv
```

### Issue: "No PDF files found in the 'pdfs' folder"

**Solution**:
1. Create `pdfs/` folder if missing:
   ```bash
   mkdir pdfs  # macOS/Linux
   # OR
   mkdir pdfs  # Windows
   ```
2. Add your PDF file to this folder
3. Ensure filename ends with `.pdf`

### Issue: "Failed to authenticate with OpenAI API"

**Solution**:
1. Verify your API key is correct (copy it again from OpenAI dashboard)
2. Check that the key starts with `sk-`
3. Ensure you have API credits: https://platform.openai.com/account/billing/overview
4. Check if key is rate limited (check OpenAI dashboard)

### Issue: "Module import failed" on FAISS

**Solution**: Use CPU version
```bash
pip uninstall faiss-cpu
pip install faiss-cpu==1.7.4
```

## Environment Setup Checklist

- [ ] Python 3.8+ installed (`python --version`)
- [ ] Virtual environment created (`venv` folder exists)
- [ ] Virtual environment activated (prompt shows `(venv)`)
- [ ] Requirements installed (`pip list` shows langchain, openai, etc.)
- [ ] `.env` file created with valid API key
- [ ] `.env` file in `.gitignore` (don't commit it!)
- [ ] PDF file in `pdfs/` folder
- [ ] Demo runs successfully with no errors

## Running the Chatbot

### Interactive Mode
```bash
cd src
python main.py
```

### Demo Mode (Test Questions)
```bash
cd src
python demo.py
```

### Using the Chatbot Class in Your Own Code
```python
from chatbot import SRMInsiderBot

# Initialize
bot = SRMInsiderBot("path/to/your.pdf")

# Load PDF
bot.load_pdf()

# Process documents
bot.process_documents()

# Ask a question
result = bot.answer_question("What is SRM INSIDER?")
print(result["answer"])
```

## Next Steps

1. ✅ Complete setup following these steps
2. ✅ Run demo to verify everything works
3. 📹 Record a demo video showing the bot answering 5 questions
4. 📊 Create a flowchart (see `ARCHITECTURE.md`)
5. 🚀 Push code to GitHub with good commit messages
6. 📦 Submit GitHub repo link

---

**Still having issues?** Check [ARCHITECTURE.md](ARCHITECTURE.md) for system details or review the main [README.md](../README.md).
