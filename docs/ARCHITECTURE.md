# SRM Insider AI Bot - Architecture & Flowchart

## System Architecture

This document explains how the PDF content flows through the chatbot system to generate answers.

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SRM INSIDER AI BOT FLOW                          │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────┐
│   PDF Document      │
│ (SRM Insider Info)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  1. PDF LOADER (PyPDFLoader)            │
│  ✓ Reads PDF file                       │
│  ✓ Extracts text from each page         │
│  ✓ Creates Document objects with        │
│    metadata (page number, etc.)         │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  2. TEXT SPLITTER                       │
│  ✓ Splits large text into chunks        │
│  ✓ Chunk size: 500 characters           │
│  ✓ Overlap: 50 characters (context)     │
│  ✓ Creates manageable pieces            │
│  Output: ~20-100 chunks (depends on PDF)│
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  3. EMBEDDING GENERATION                │
│  ✓ OpenAI Embeddings API                │
│  ✓ Converts each chunk to vector        │
│  ✓ 1536-dimensional vector              │
│  ✓ Captures semantic meaning             │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  4. VECTOR STORE (FAISS)                │
│  ✓ Stores all embeddings                │
│  ✓ Creates index for fast search        │
│  ✓ Enables similarity search            │
│  ✓ In-memory database                   │
└──────────┬──────────────────────────────┘
           │
           ▼
        [READY FOR QUERIES]
           │
           ▼
┌──────────────────────────┐
│  USER ASKS QUESTION      │
│  "What is SRM INSIDER?"  │
└──────────┬───────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  5. QUESTION EMBEDDING                  │
│  ✓ Convert question to embedding        │
│  ✓ Same embedding model as documents    │
│  ✓ Creates comparable vector            │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  6. SIMILARITY SEARCH                   │
│  ✓ Find k=3 most similar chunks         │
│  ✓ Use cosine similarity                │
│  ✓ Retrieve relevant context            │
│  ✓ Return source pages                  │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  7. PROMPT CONSTRUCTION                 │
│  ✓ System prompt + relevant context     │
│  ✓ User question                        │
│  ✓ Instruction to use only provided     │
│    context                              │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  8. LLM (GPT-3.5-turbo)                 │
│  ✓ Process prompt with context          │
│  ✓ Generate answer based on chunks      │
│  ✓ Temperature: 0.5 (balanced)          │
│  ✓ Uses OpenAI API                      │
└──────────┬──────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────┐
│  9. RESPONSE ASSEMBLY                   │
│  ✓ Format answer text                   │
│  ✓ Include source document references   │
│  ✓ Add page numbers                     │
└──────────┬──────────────────────────────┘
           │
           ▼
┌──────────────────────────┐
│   USER RECEIVES ANSWER   │
│   with Sources & Pages   │
└──────────────────────────┘
```

## Component Details

### 1. PDF Loader
- **Library**: PyPDFLoader (from langchain)
- **Input**: PDF file path
- **Output**: List of Document objects
- **Process**: 
  - Opens PDF file
  - Extracts text from each page
  - Preserves metadata (page numbers)

### 2. Text Splitter
- **Type**: RecursiveCharacterTextSplitter
- **Configuration**:
  - `chunk_size=500`: Each chunk is max 500 characters
  - `chunk_overlap=50`: 50 char overlap for context preservation
  - `separators`: ["\n\n", "\n", " ", ""] (prioritize sentence/paragraph breaks)
- **Purpose**: Create optimal-sized pieces for embedding

### 3. Embeddings
- **Provider**: OpenAI Embeddings API
- **Model**: text-embedding-3-small (default)
- **Output**: 1536-dimensional vectors
- **Cost**: ~$0.00002 per 1K tokens
- **Purpose**: Convert text to numerical representation for similarity search

### 4. Vector Store (FAISS)
- **Library**: FAISS (Facebook AI Similarity Search)
- **Type**: In-memory vector database
- **Index Type**: Flat index (exact search)
- **Advantages**:
  - Fast similarity search
  - No external database needed
  - Easy to use for beginners
- **Retrieval**: Returns k=3 most similar chunks

### 5. Retrieval Chain (RetrievalQA)
- **Type**: stuff chain (concatenate context)
- **Flow**:
  1. Convert question to embedding
  2. Search vector store for similar chunks
  3. Retrieve 3 most relevant chunks
  4. Combine with system prompt
  5. Send to LLM

### 6. Language Model
- **Provider**: OpenAI
- **Model**: gpt-3.5-turbo
- **Temperature**: 0.5 (balanced between deterministic and creative)
- **Purpose**: Generate natural language answer from context

## Key Concepts

### Embeddings
Embeddings are numerical representations of text that capture semantic meaning. Similar texts have similar embeddings, allowing vector search.

```
"What is SRM INSIDER?" → [0.123, -0.456, 0.789, ...]  (1536 numbers)
"SRM INSIDER is..." → [0.120, -0.458, 0.791, ...]      (similar!)
```

### Vector Similarity
FAISS uses cosine similarity to find chunks most relevant to the question:

```
Similarity = cos(question_embedding, chunk_embedding)
Range: -1 (opposite) to 1 (identical)
```

### Context Window
The prompt sent to GPT-3.5-turbo includes:
- System instruction
- Top 3 relevant chunks from PDF
- User's question

```
System: "You are an expert about SRM INSIDER. Answer based only on the provided context."
Context: [3 most relevant chunks from PDF]
Question: "What is SRM INSIDER?"
```

## API Costs

### Estimate for SRM Insider Bot

| Operation | Tokens | Cost |
|-----------|--------|------|
| Embed 10-page PDF (first run) | ~5,000 | $0.10 |
| Each question (embed + LLM) | ~1,500 | $0.03 |
| 5 test questions | ~7,500 | $0.15 |

**Typical cost per 100 questions**: ~$3

## Error Handling

The system handles failures gracefully:

```
PDF Loading Error → User message: "PDF file not found"
API Key Missing → User message: "OPENAI_API_KEY not found"
API Rate Limit → Retry with exponential backoff
Network Error → User message: "Error connecting to OpenAI API"
```

## Performance Optimization

### Current Optimizations
- **Caching**: Embeddings computed once, reused for all questions
- **Batch Processing**: Multiple questions can be asked without reloading PDF
- **Efficient Search**: FAISS provides O(log n) search complexity

### Potential Improvements
- Store embeddings on disk to avoid recomputing
- Use smaller embedding model for faster inference
- Implement query expansion to find more relevant chunks
- Use multi-query retrieval for complex questions

## Security Considerations

1. **API Keys**: Never commit `.env` files (protected by `.gitignore`)
2. **User Privacy**: No conversation history is logged by default
3. **PDF Content**: Processed on-device, not stored
4. **Rate Limiting**: Use OpenAI's rate limits to prevent abuse

## Limitations & Considerations

1. **PDF Quality**: Works best with text-based PDFs, not scanned images
2. **Document Length**: Tested up to 10 pages; larger documents may be slower
3. **Context Length**: Only top 3 chunks used (due to token limits)
4. **API Dependency**: Requires internet connection and valid API key
5. **Cost**: Each question incurs API charges

---

**For visual representation, see the flowchart in the docs folder.**
