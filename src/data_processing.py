"""
Functions for loading and processing Markdown documents from the Obsidian vault.

Includes:
- Loading .md files (Step 2).
- Extracting Obsidian links and adding relative paths (Step 3).
- Splitting documents into chunks (Step 4).

Based on guide.md steps 2, 3, and 4.
"""

import os
import logging
import regex as re
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src import config

# Configure logging (consistent with rag_components)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_markdown_docs(vault_path: str) -> list[Document]:
    """Loads all markdown documents from the specified vault path."""
    if not vault_path or not os.path.isdir(vault_path):
        logging.error(f"Invalid Obsidian Vault Path: {vault_path}")
        raise ValueError(f"Obsidian vault path is not a valid directory: {vault_path}")

    logging.info(f"Loading documents from: {vault_path}")
    loader = DirectoryLoader(
        vault_path,
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
        show_progress=True,
        use_multithreading=True,
        silent_errors=True, # Log errors instead of failing hard
    )
    try:
        docs_raw = loader.load()
        logging.info(f"Loaded {len(docs_raw)} raw documents.")
        if not docs_raw:
            logging.warning(f"No markdown documents found in {vault_path}. Ensure the path is correct and contains .md files.")
        return docs_raw
    except Exception as e:
        logging.error(f"Failed to load documents: {e}")
        raise

def _extract_obsidian_links(text: str) -> list[str]:
    """Finds all Obsidian-style [[wikilinks]] in the text."""
    # Basic regex: [[any characters not closing brackets]]
    # Captures content inside brackets, handling aliases [[link|alias]]
    try:
        matches = re.findall(r'\[\[(.*?)\]\]', text)
        # Future enhancement: Split alias, e.g., link = m.split('|')[0]
        return matches
    except Exception as e:
        logging.warning(f"Regex error extracting links: {e}")
        return []

def process_docs_metadata(docs_raw: list[Document], vault_path: str) -> list[Document]:
    """Adds relative path and extracts Obsidian links for each document."""
    processed_docs = []
    logging.info(f"Processing metadata for {len(docs_raw)} documents...")
    for doc in docs_raw:
        try:
            full_path = doc.metadata.get('source', '')
            if vault_path and full_path and vault_path in full_path:
                # Normalize paths for reliable comparison/relpath calculation
                norm_vault_path = os.path.normpath(vault_path)
                norm_full_path = os.path.normpath(full_path)
                # Ensure the full path starts with the vault path before making relative
                if norm_full_path.startswith(norm_vault_path):
                   relative_path = os.path.relpath(norm_full_path, norm_vault_path)
                else:
                   logging.warning(f"Document path {norm_full_path} not relative to vault {norm_vault_path}, using full path.")
                   relative_path = norm_full_path
            else:
                relative_path = full_path # Fallback

            links = _extract_obsidian_links(doc.page_content)

            new_metadata = doc.metadata.copy()
            new_metadata['relative_path'] = relative_path
            new_metadata['obsidian_links'] = links

            processed_docs.append(Document(page_content=doc.page_content, metadata=new_metadata))
        except Exception as e:
            logging.error(f"Error processing metadata for doc {doc.metadata.get('source')}: {e}")
            # Optionally skip the doc or add with minimal metadata
            continue # Skip problematic doc

    logging.info(f"Finished processing metadata for {len(processed_docs)} documents.")
    if docs_raw and not processed_docs:
         logging.warning("No documents were successfully processed for metadata.")
    elif processed_docs:
        logging.debug(f"Example processed doc metadata: {processed_docs[0].metadata}")
    return processed_docs

def split_documents(processed_docs: list[Document]) -> list[Document]:
    """Splits the processed documents into chunks."""
    logging.info(f"Splitting {len(processed_docs)} documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        length_function=len,
        is_separator_regex=False,
        # separators=["\n\n", "\n", " ", "", "\n# ", "\n## ", "\n### "] # Consider markdown separators
    )
    try:
        chunks = text_splitter.split_documents(processed_docs)
        logging.info(f"Split documents into {len(chunks)} chunks.")
        if chunks:
            logging.debug(f"Example chunk metadata: {chunks[0].metadata}")
        if not chunks and processed_docs:
             logging.warning("Processed documents but generated zero chunks. Check chunk size/overlap and document content.")
        return chunks
    except Exception as e:
        logging.error(f"Error splitting documents: {e}")
        raise

# Example usage (for testing this module directly)
# if __name__ == '__main__':
#     print("Testing data processing...")
#     try:
#         raw_docs = load_markdown_docs(config.OBSIDIAN_VAULT_PATH)
#         if raw_docs:
#             processed = process_docs_metadata(raw_docs, config.OBSIDIAN_VAULT_PATH)
#             if processed:
#                 chunks = split_documents(processed)
#                 print(f"Successfully processed and split into {len(chunks)} chunks.")
#             else:
#                 print("Metadata processing yielded no documents.")
#         else:
#             print("Loading yielded no documents.")
#     except Exception as e:
#         print(f"An error occurred during testing: {e}")
#     except ValueError as ve:
#         print(f"Configuration error: {ve}")