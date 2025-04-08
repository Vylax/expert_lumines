"""
Main execution script for the RAG application.

Orchestrates the RAG pipeline:
- Loads configuration.
- Loads and processes documents.
- Initializes RAG components (embeddings, vector store, retriever, LLM).
- Builds the RAG chain.
- Handles user queries and invokes the chain to get answers (Step 11).

Connects functionalities from src/config.py, src/data_processing.py,
src/rag_components.py, and src/chain.py.
Also relates to environment setup in Step 1.
"""
