# System Flowchart - SRM Insider AI Bot

This document contains visual flowcharts showing how the system works.

## Complete System Flowchart

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          SRM INSIDER AI BOT                             │
│                        Complete System Flow                             │
└─────────────────────────────────────────────────────────────────────────┘

                            ┌──────────────┐
                            │  PDF File    │
                            │  (SRM Info)  │
                            └──────┬───────┘
                                   │
                    ┌──────────────▼─────────────┐
                    │   1. PDF LOADER            │
                    │  ┌──────────────────────┐  │
                    │  │ PyPDFLoader          │  │
                    │  │ - Open PDF           │  │
                    │  │ - Extract text       │  │
                    │  │ - Keep page metadata │  │
                    │  └──────────────────────┘  │
                    └──────────────┬─────────────┘
                                   │
                    ┌──────────────▼─────────────┐
                    │   2. TEXT SPLITTER         │
                    │  ┌──────────────────────┐  │
                    │  │ RecursiveCharacter   │  │
                    │  │ - Size: 500 chars    │  │
                    │  │ - Overlap: 50 chars  │  │
                    │  │ - Output: ~20-100    │  │
                    │  │   chunks             │  │
                    │  └──────────────────────┘  │
                    └──────────────┬─────────────┘
                                   │
                    ┌──────────────▼─────────────┐
                    │   3. EMBEDDINGS            │
                    │  ┌──────────────────────┐  │
                    │  │ OpenAI Embeddings    │  │
                    │  │ - Model: text-embed  │  │
                    │  │ - Output: 1536D vec  │  │
                    │  │ - Semantic meaning   │  │
                    │  └──────────────────────┘  │
                    └──────────────┬─────────────┘
                                   │
                    ┌──────────────▼─────────────┐
                    │   4. VECTOR STORE          │
                    │  ┌──────────────────────┐  │
                    │  │ FAISS Index          │  │
                    │  │ - Store embeddings   │  │
                    │  │ - Fast similarity    │  │
                    │  │ - Ready for query    │  │
                    │  └──────────────────────┘  │
                    └──────────────┬─────────────┘
                                   │
                                   │
                        ╔══════════▼══════════╗
                        ║  SYSTEM READY       ║
                        ║  For Questions      ║
                        ╚════════════════════╝
                                   │
                                   │
                ┌──────────────────┴──────────────────┐
                │                                     │
    ┌───────────▼──────────┐          ┌──────────────▼─────────┐
    │  INTERACTIVE MODE    │          │  AUTOMATED DEMO MODE   │
    │  (main.py)           │          │  (demo.py)             │
    │                      │          │                        │
    │  User Input → Q      │          │  Loop 5 Questions      │
    └───────┬──────────────┘          └──────────┬─────────────┘
            │                                     │
            │                                     │
            ├─────────────────┬───────────────────┤
                              │
                ┌─────────────▼──────────────┐
                │  5. EMBED QUESTION         │
                │  ┌──────────────────────┐  │
                │  │ Convert Q to vector  │  │
                │  │ Same model as docs   │  │
                │  │ Create 1536D vector  │  │
                │  └──────────────────────┘  │
                └─────────────┬──────────────┘
                              │
                ┌─────────────▼──────────────┐
                │  6. SIMILARITY SEARCH      │
                │  ┌──────────────────────┐  │
                │  │ FAISS Search         │  │
                │  │ - Find k=3 matches   │  │
                │  │ - Cosine similarity  │  │
                │  │ - Get page #         │  │
                │  └──────────────────────┘  │
                └─────────────┬──────────────┘
                              │
                ┌─────────────▼──────────────────┐
                │  7. BUILD CONTEXT             │
                │  ┌──────────────────────────┐  │
                │  │ System Prompt            │  │
                │  │ + 3 Relevant Chunks     │  │
                │  │ + User Question         │  │
                │  └──────────────────────────┘  │
                └─────────────┬──────────────────┘
                              │
                ┌─────────────▼──────────────────┐
                │  8. LLM PROCESSING             │
                │  ┌──────────────────────────┐  │
                │  │ GPT-3.5-turbo (OpenAI) │  │
                │  │ - Temp: 0.5 (balanced) │  │
                │  │ - Generate answer      │  │
                │  │ - API call             │  │
                │  └──────────────────────────┘  │
                └─────────────┬──────────────────┘
                              │
                ┌─────────────▼──────────────────┐
                │  9. FORMAT RESPONSE            │
                │  ┌──────────────────────────┐  │
                │  │ Answer Text              │  │
                │  │ + Source Pages           │  │
                │  │ + Metadata               │  │
                │  └──────────────────────────┘  │
                └─────────────┬──────────────────┘
                              │
                ┌─────────────▼──────────────┐
                │  USER SEES ANSWER          │
                │  ┌────────────────────────┐ │
                │  │ "SRM INSIDER is..."    │ │
                │  │ Sources: Pages 1, 2    │ │
                │  └────────────────────────┘ │
                └────────────────────────────┘
```

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                   EXTERNAL SERVICES                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────────┐      ┌──────────────────────────┐   │
│  │  OpenAI API          │      │  File System             │   │
│  │  - Embeddings        │      │  - PDF files             │   │
│  │  - GPT-3.5-turbo     │      │  - .env file             │   │
│  │  - Tokens limit      │      │  - Vector index          │   │
│  └──────────────────────┘      └──────────────────────────┘   │
│                                                                 │
└────────────────┬──────────────────────────────────┬────────────┘
                 │                                  │
        ┌────────▼─────────┐              ┌─────────▼────────┐
        │ LANGCHAIN        │              │ LOCAL DATA       │
        │ Framework        │              │ FAISS Index      │
        └────────┬─────────┘              └────────────────┬──┘
                 │                                       │
    ┌────────────▼──────────────────────────────────────▼──┐
    │        SRMInsiderBot Class (chatbot.py)              │
    │                                                      │
    │  ┌─────────────────────────────────────────────┐   │
    │  │ Public Methods:                              │   │
    │  │ - load_pdf(path)                             │   │
    │  │ - process_documents()                        │   │
    │  │ - answer_question(q)                         │   │
    │  │ - interactive_chat()                         │   │
    │  └─────────────────────────────────────────────┘   │
    │                                                      │
    │  ┌─────────────────────────────────────────────┐   │
    │  │ Internal State:                              │   │
    │  │ - documents: Document[]                      │   │
    │  │ - vector_store: FAISS                        │   │
    │  │ - qa_chain: RetrievalQA                      │   │
    │  │ - api_key: str                               │   │
    │  └─────────────────────────────────────────────┘   │
    └────────────────┬──────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
    ┌───▼────┐  ┌────▼─────┐  ┌─▼──────┐
    │ main.py│  │ demo.py  │  │other.py│
    │Interact│  │Test 5 Qs │  │ Apps   │
    └────────┘  └──────────┘  └────────┘
```

## Data Flow Sequence Diagram

```
User            App             Chatbot          Vector Store       LLM
 │               │                 │                   │              │
 │  Ask Question │                 │                   │              │
 ├──────────────>│                 │                   │              │
 │               │  Embed Q        │                   │              │
 │               ├────────────────>│                   │              │
 │               │                 │                   │              │
 │               │                 │  Search Similar   │              │
 │               │                 ├──────────────────>│              │
 │               │                 │<──────────────────┤              │
 │               │                 │  Return 3 chunks  │              │
 │               │                 │                   │              │
 │               │  Build Context  │                   │              │
 │               ├────────────────>│                   │              │
 │               │                 │                   │              │
 │               │ Send to LLM (Q + Context)          │              │
 │               ├───────────────────────────────────────────────────>│
 │               │                 │                   │              │
 │               │                 │                   │  Generate   │
 │               │                 │                   │<─────────────┤
 │               │                 │                   │   Answer    │
 │               │<───────────────────────────────────────────────────┤
 │               │  Format Result  │                   │              │
 │               ├──────────────────────────────────────────────────> │
 │<──────────────┤                 │                   │              │
 │  Display      │                 │                   │              │
 │  Answer       │                 │                   │              │
 │               │                 │                   │              │
```

## Detailed Processing Pipeline

```
INPUT: "What is SRM INSIDER?"
│
├─ Step 1: Tokenization
│  └─ ["What", "is", "SRM", "INSIDER", "?"]
│
├─ Step 2: Embedding Generation
│  └─ Query Vector: [0.145, -0.234, 0.567, ..., 0.089]  (1536 dims)
│
├─ Step 3: Vector Similarity Search
│  │
│  ├─ Compare with Chunk 1 → Similarity: 0.87
│  ├─ Compare with Chunk 2 → Similarity: 0.92 ✓ (Top 1)
│  ├─ Compare with Chunk 3 → Similarity: 0.78
│  ├─ ... (continue for all chunks)
│  │
│  └─ Return Top 3 Chunks
│     1. Chunk 2 (0.92)
│     2. Chunk 5 (0.85)
│     3. Chunk 8 (0.81)
│
├─ Step 4: Prompt Assembly
│  │
│  └─ """System: Answer based on context.
│     
│     Context:
│     [Chunk 2 content from PDF page 1]
│     [Chunk 5 content from PDF page 3]
│     [Chunk 8 content from PDF page 2]
│     
│     Question: What is SRM INSIDER?
│     
│     Answer:"""
│
├─ Step 5: LLM Processing
│  │
│  └─ OpenAI API Call
│     ├─ Model: gpt-3.5-turbo
│     ├─ Temperature: 0.5
│     ├─ Max tokens: 500
│     └─ [API processing...]
│
└─ OUTPUT: "SRM INSIDER is a premier community platform dedicated to..."
   └─ Sources: Pages 1, 3, 2
```

## Component Interaction Matrix

```
┌─────────────────┬─────────────┬──────────────┬─────────────────┐
│ Component       │ Input       │ Processing   │ Output          │
├─────────────────┼─────────────┼──────────────┼─────────────────┤
│ PDF Loader      │ File path   │ Extract text │ Document list   │
│ Text Splitter   │ Documents   │ Chunk text   │ Chunks          │
│ Embeddings      │ Text chunks │ Vectorize    │ Vectors (1536D) │
│ FAISS           │ Vectors     │ Index/Search │ Top K similar   │
│ Prompt Builder  │ Q + context │ Format       │ LLM prompt      │
│ LLM (GPT-3.5)   │ Prompt      │ Generate     │ Answer text     │
│ Formatter       │ LLM output  │ Format       │ Final response  │
└─────────────────┴─────────────┴──────────────┴─────────────────┘
```

## Performance Pipeline

```
Request: "What is SRM INSIDER?"
│
├─ T0: 0ms      - Request received
├─ T1: 50ms     - Tokenization complete
├─ T2: 150ms    - Embedding generated (OpenAI API)
├─ T3: 160ms    - Vector search complete (FAISS local)
├─ T4: 165ms    - Context retrieved
├─ T5: 170ms    - Prompt built
├─ T6: 2000ms   - LLM response received (OpenAI API)
├─ T7: 2010ms   - Response formatted
│
└─ Total Time: ~2000ms (2 seconds)
   - Network I/O: ~1900ms (95%)
   - Local Processing: ~100ms (5%)
```

## Error Handling Flow

```
                  ┌──────────────────┐
                  │  User Question   │
                  └────────┬─────────┘
                           │
                  ┌────────▼──────────┐
                  │  Try Processing   │
                  └────────┬──────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
         ┌────▼───┐   ┌────▼────┐  ┌───▼─────┐
         │ PDF    │   │ API     │  │ Vector  │
         │ Error  │   │ Error   │  │ Error   │
         └────┬───┘   └────┬────┘  └────┬────┘
              │            │            │
              └────┬───────┴────────┬───┘
                   │                │
         ┌─────────▼───────────────▼──────┐
         │  Format Error Message          │
         │  Return to User                │
         └────────────────────────────────┘
```

---

**Legend:**
- `→` = Process flow
- `≤─` = Data input
- `─→` = Data output
- `└─` = Connection point

These flowcharts illustrate the complete data pipeline from PDF upload through AI-generated answers.
