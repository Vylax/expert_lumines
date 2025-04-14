"""
Main execution script for the RAG application.

Orchestrates the RAG pipeline:
- Loads configuration.
- Checks environment (GCP Project ID).
- Optionally forces data reprocessing.
- Loads and processes documents (if needed).
- Creates or loads the vector store.
- Creates the retriever.
- Builds the RAG chain.
- Handles user queries (either predefined or interactive) and invokes the chain.

Connects functionalities from src/config.py, src/data_processing.py,
src/rag_components.py, and src/chain.py.
"""

import os
import sys
import argparse
import logging
from src import config
from src.data_processing import load_markdown_docs, process_docs_metadata, split_documents
from src.rag_components import get_embedding_model
from src.chain import build_rag_chain
from langchain_chroma import Chroma

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main(force_reprocess: bool, query: str | None):
    """Runs the main RAG pipeline."""

    # --- 1. Configuration and Environment Checks ---
    logging.info("Starting RAG application...")
    if not config.GOOGLE_CLOUD_PROJECT:
        logging.error("GOOGLE_CLOUD_PROJECT environment variable not set in .env file.")
        sys.exit(1) # Exit if critical config is missing
    logging.info(f"Using GCP Project: {config.GOOGLE_CLOUD_PROJECT}")

    if not os.path.isdir(config.OBSIDIAN_VAULT_PATH):
        logging.error(f"Obsidian vault path not found or not a directory: {config.OBSIDIAN_VAULT_PATH}")
        sys.exit(1)

    vectorstore_exists = os.path.isdir(config.VECTORSTORE_PATH)
    logging.info(f"Vector store path: {config.VECTORSTORE_PATH} (Exists: {vectorstore_exists})")

    # --- 2. Initialize Embedding Model (needed for both creation and loading) ---
    try:
        embeddings = get_embedding_model()
    except Exception as e:
        logging.error(f"Failed to initialize embedding model: {e}. Exiting.")
        sys.exit(1)

    # --- 3. Data Processing & Vector Store Creation/Loading (Steps 2-6) ---
    vectorstore = None
    if force_reprocess or not vectorstore_exists:
        logging.info("Processing data and creating new vector store...")
        try:
            # Steps 2, 3, 4
            raw_docs = load_markdown_docs(config.OBSIDIAN_VAULT_PATH)
            if not raw_docs:
                 logging.warning("No documents loaded. Vector store will be empty or loading will fail.")
                 # Depending on desired behavior, could exit or continue with empty store
            processed_docs = process_docs_metadata(raw_docs, config.OBSIDIAN_VAULT_PATH)
            chunks = split_documents(processed_docs)

            if not chunks:
                 logging.warning("No chunks generated after processing. Vector store cannot be created.")
                 # Decide if to proceed with an empty store or exit
                 if not vectorstore_exists: # If store HAS to be created, exit
                     logging.error("Cannot create vector store with no data.")
                     sys.exit(1)
                 else: # If store exists, we might be able to load it (though force_reprocess implies we shouldn't)
                     logging.warning("Proceeding without creating new vector store due to lack of chunks.")

            # Step 6 (Create)
            if chunks: # Only create if there's data
                logging.info(f"Creating Chroma vector store at {config.VECTORSTORE_PATH}...")
                # Ensure the parent directory exists
                vectorstore_dir = os.path.dirname(config.VECTORSTORE_PATH)
                if vectorstore_dir and not os.path.exists(vectorstore_dir):
                    logging.info(f"Creating directory: {vectorstore_dir}")
                    os.makedirs(vectorstore_dir)

                vectorstore = Chroma.from_documents(
                    documents=chunks,
                    embedding=embeddings,
                    persist_directory=config.VECTORSTORE_PATH
                )
                logging.info("Vector store created successfully.")
            else:
                 # If we couldn't create chunks and the store doesn't exist, we must exit
                 if not vectorstore_exists:
                     logging.error("Failed to create vector store: No data chunks produced.")
                     sys.exit(1)
                 # If we were forced to reprocess but got no chunks, try loading existing?
                 # This edge case might need refinement based on desired behavior.
                 logging.warning("Force reprocess yielded no data, attempting to load existing store...")

        except Exception as e:
            logging.error(f"Error during data processing or vector store creation: {e}")
            sys.exit(1)

    # Load existing store if not created above
    if vectorstore is None:
        if vectorstore_exists:
            logging.info(f"Loading existing Chroma vector store from {config.VECTORSTORE_PATH}...")
            try:
                # Step 6 (Load)
                vectorstore = Chroma(
                    persist_directory=config.VECTORSTORE_PATH,
                    embedding_function=embeddings
                )
                logging.info("Vector store loaded successfully.")
            except Exception as e:
                logging.error(f"Error loading vector store: {e}. Try running with --force-reprocess.")
                sys.exit(1)
        else:
            # This should ideally be caught earlier, but as a safeguard:
            logging.error("Vector store not found and could not be created. Exiting.")
            sys.exit(1)

    # --- 4. Create Retriever (Step 7) ---
    logging.info("Creating retriever...")
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": config.RETRIEVER_K}
    )
    logging.info(f"Retriever created with k={config.RETRIEVER_K}.")

    # --- 5. Build RAG Chain (Step 10) ---
    try:
        rag_chain = build_rag_chain(retriever)
    except Exception as e:
        logging.error(f"Failed to build RAG chain: {e}. Exiting.")
        sys.exit(1)

    # --- 6. Query the System (Step 11) ---
    if query:
        # Use the query provided via command line argument
        logging.info(f"Processing provided query: '{query}'")
        try:
            response = rag_chain.invoke(query)
            print("\nResponse:")
            print(response)
        except Exception as e:
            logging.error(f"An error occurred during query invocation: {e}")
    else:
        # Enter interactive query loop
        logging.info("Entering interactive query mode. Type 'quit' or 'exit' to stop.")
        while True:
            try:
                user_question = input("\nEnter your question: ")
                if user_question.lower() in ['quit', 'exit']:
                    logging.info("Exiting interactive mode.")
                    break
                if not user_question:
                    continue

                logging.info(f"Invoking RAG chain with question: '{user_question}'")
                response = rag_chain.invoke(user_question)
                print("\nResponse:")
                print(response)

            except EOFError: # Handle Ctrl+D
                 logging.info("Exiting interactive mode (EOF received).")
                 break
            except KeyboardInterrupt: # Handle Ctrl+C
                 logging.info("\nExiting interactive mode (KeyboardInterrupt).")
                 break
            except Exception as e:
                 logging.error(f"An error occurred during interactive query: {e}")
                 # Optionally continue the loop or break depending on severity

    logging.info("RAG application finished.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query your Obsidian vault using a RAG pipeline.")
    parser.add_argument(
        "-f", "--force-reprocess",
        action="store_true",
        help="Force reloading and reprocessing of all documents, overwriting the existing vector store."
    )
    parser.add_argument(
        "-q", "--query",
        type=str,
        default=None,
        help="Ask a single question and exit. If not provided, enters interactive mode."
    )
    args = parser.parse_args()

    try:
        main(force_reprocess=args.force_reprocess, query=args.query)
    except ValueError as ve:
        logging.error(f"Configuration or Value Error: {ve}")
        sys.exit(1)
    except ImportError as ie:
        logging.error(f"Import Error: {ie}. Please ensure all dependencies are installed from requirements.txt")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred in the main execution: {e}")
        import traceback
        traceback.print_exc() # Print full traceback for unexpected errors
        sys.exit(1)
