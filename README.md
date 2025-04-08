# expert_lumines

## Folder Structure

```
expert_lumines/
│
├── .venv/                   # Virtual environment
│
├── data/
│   └── chroma_db_obsidian/  # ChromaDB persistence directory
│
├── src/
│   ├── __init__.py
│   ├── config.py            # Configurations (paths, models, etc.)
│   ├── data_processing.py   # Document loading and preprocessing
│   ├── rag_components.py    # Setup for embeddings, vector store, retriever, LLM, prompt
│   └── chain.py             # RAG chain definition (LCEL)
│
├── .env                     # Environment variables (API keys, Project ID)
├── requirements.txt         # Python dependencies
├── main.py                  # Main application script
└── guide.md                 # Project guide and setup instructions
```
