"""
Functions for initializing and configuring the RAG components.

Sets up:
- Embedding model (VertexAIEmbeddings - Step 5).
- Vector store (ChromaDB, creation/loading - Step 6).
- Retriever (from vector store - Step 7).
- Prompt template and context formatting (Step 8).
- Language model (ChatVertexAI - Step 9).

Based on guide.md steps 5, 6, 7, 8, and 9.
"""
