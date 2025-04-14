"""
Functions for loading, processing, and splitting documents.

Handles:
- Loading markdown files from the specified directory (Step 2).
- Extracting metadata like relative paths and Obsidian links (Step 3).
- Splitting documents into smaller chunks for embedding (Step 4).

Based on guide.md steps 2, 3, and 4.
"""

import os
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_core.documents import Document
import regex as re
from src import config # Import the config module

# --- Load documents using path from config ---
print(f"Loading documents from: {config.OBSIDIAN_VAULT_PATH}")
# Optional: Rely on the check within config.py

loader = DirectoryLoader(
    config.OBSIDIAN_VAULT_PATH,
    glob="**/*.md",         # Load only markdown files recursively
    loader_cls=UnstructuredMarkdownLoader,
    show_progress=True,
    use_multithreading=True # Can speed up loading
)
docs_raw = loader.load()
print(f"Loaded {len(docs_raw)} raw documents.")

def extract_obsidian_links(text):
    """Finds all Obsidian-style [[wikilinks]] in the text."""
    # Basic regex: [[any characters not closing brackets]]
    # It captures the content inside the brackets.
    # Handles potential aliases [[link|alias]] by capturing 'link|alias'
    # You might want to refine this to only capture 'link' if aliases exist.
    matches = re.findall(r'\[\[(.*?)\]\]', text)
    # Simple approach: return the full match inside brackets for now
    return matches # e.g., ['Note A', 'Another Note|Alias']

processed_docs = []
for doc in docs_raw:
    # Create relative path from vault root for cleaner metadata
    full_path = doc.metadata.get('source', '')
    # Use the config path for correct relative path calculation
    # Add a check for config.OBSIDIAN_VAULT_PATH to avoid errors if it's None/empty
    if config.OBSIDIAN_VAULT_PATH and config.OBSIDIAN_VAULT_PATH in full_path:
         relative_path = os.path.relpath(full_path, config.OBSIDIAN_VAULT_PATH)
    else:
         relative_path = full_path # Fallback if path seems odd

    # Extract links from the page content
    links = extract_obsidian_links(doc.page_content)

    # Update metadata - important to copy existing metadata
    new_metadata = doc.metadata.copy()
    new_metadata['relative_path'] = relative_path
    new_metadata['obsidian_links'] = links # Store the list of link targets

    # Create a new Document or update in place (creating new is safer)
    # Ensure 'Document' is imported (from langchain_core.documents)
    processed_docs.append(Document(page_content=doc.page_content, metadata=new_metadata))

print(f"Processed metadata for {len(processed_docs)} documents.")
# Optional: Print an example to verify metadata
if processed_docs:
    print("Example processed doc metadata:", processed_docs[0].metadata)