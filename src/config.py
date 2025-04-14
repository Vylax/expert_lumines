"""
Configuration settings for the RAG application.

Contains configuration variables like file paths and model names,
and loads sensitive information (API keys, project IDs) from the .env file.
Corresponds to parts of Step 1 (loading GOOGLE_CLOUD_PROJECT) and variables
used in Steps 2, 5, 6, and 9 from guide.md.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file (especially for secrets)
load_dotenv()

# --- Paths ---
# !! IMPORTANT: Update this path to your actual Obsidian vault location !!
OBSIDIAN_VAULT_PATH = "./data/sample_vault"
VECTORSTORE_PATH = "./data/chroma_db_obsidian"      # Relative to project root

# --- Model Names ---
# Check Vertex AI documentation for recommended model versions
EMBEDDING_MODEL_NAME = "text-embedding-004"
LLM_MODEL_NAME = "gemini-2.0-flash-lite"
LLM_TEMPERATURE = 0.2

# --- Data Processing ---
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

# --- Retriever ---
RETRIEVER_K = 5 # Number of chunks to retrieve

# --- Secrets / Environment Variables ---
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")

# --- Sanity Checks (Optional but Recommended) ---
if not GOOGLE_CLOUD_PROJECT:
    print("Warning: GOOGLE_CLOUD_PROJECT environment variable not set in .env file.")

if not os.path.isdir(OBSIDIAN_VAULT_PATH):
    print(f"Warning: OBSIDIAN_VAULT_PATH does not exist or is not a directory: {OBSIDIAN_VAULT_PATH}")
    # Consider raising an error here depending on your application's needs