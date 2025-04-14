"""
Defines the LangChain Expression Language (LCEL) RAG chain.

Combines the retriever, prompt, and language model into a
single runnable chain.

Based on guide.md Step 10.
"""
import logging
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever
from src.rag_components import get_prompt_template, get_llm, format_docs_with_metadata
from src import config # To ensure config is loaded for components

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def build_rag_chain(retriever: VectorStoreRetriever):
    """Builds the RAG chain using the provided retriever and configured components."""
    if not config.GOOGLE_CLOUD_PROJECT:
        logging.error("GOOGLE_CLOUD_PROJECT not set in environment. Cannot initialize LLM.")
        raise ValueError("GOOGLE_CLOUD_PROJECT environment variable not set.")

    logging.info("Building the RAG chain...")

    # Retrieve necessary components
    try:
        prompt = get_prompt_template()
        llm = get_llm() # Requires GOOGLE_CLOUD_PROJECT
    except Exception as e:
        logging.error(f"Failed to retrieve LLM or Prompt components: {e}")
        raise

    # Define the RAG pipeline using LCEL
    rag_chain = (
        # RunnablePassthrough allows chaining while passing the original input (question)
        # RunnableLambda integrates our custom formatting function
        {"context": retriever | RunnableLambda(format_docs_with_metadata), "question": RunnablePassthrough()}
        | prompt         # Pass the dictionary to the prompt template
        | llm            # Pass the formatted prompt to the LLM
        | StrOutputParser() # Parse the LLM's AIMessage output to a string
    )
    logging.info("RAG chain built successfully.")
    return rag_chain

# Example of how the chain might be built (potentially called from main.py)
# if __name__ == '__main__':
#     # This block requires a vector store and retriever to be set up first
#     # It's primarily for demonstrating the chain building in isolation or for testing
#     print("Attempting to build chain (requires dependencies like vector store)...")
#     try:
#         # --- Dummy Retriever Setup (Replace with actual setup from main.py) ---
#         # Needs imports: Chroma, get_embedding_model
#         from langchain_chroma import Chroma
#         from src.rag_components import get_embedding_model
#         print(f"Using vector store path: {config.VECTORSTORE_PATH}")
#         if not os.path.exists(config.VECTORSTORE_PATH):
#              print("ERROR: Vector store path does not exist. Run data loading first.")
#              exit(1)
#         if not config.GOOGLE_CLOUD_PROJECT:
#             print("ERROR: GOOGLE_CLOUD_PROJECT not set.")
#             exit(1)

#         print("Initializing embedding model...")
#         embedding_function = get_embedding_model()
#         print("Loading vector store...")
#         vectorstore = Chroma(
#              persist_directory=config.VECTORSTORE_PATH,
#              embedding_function=embedding_function
#         )
#         print("Creating retriever...")
#         retriever = vectorstore.as_retriever(search_kwargs={"k": config.RETRIEVER_K})
#         # --- End Dummy Setup ---

#         print("Building chain...")
#         chain = build_rag_chain(retriever)
#         print("Chain built successfully.")

#         # Example query using the built chain
#         question = "What is the purpose of the config file?"
#         print(f"\nInvoking chain with question: '{question}'")
#         response = chain.invoke(question)
#         print("\nResponse:")
#         print(response)

#     except ImportError as ie:
#          print(f"Import Error: {ie}. Ensure all dependencies are installed.")
#     except ValueError as ve:
#          print(f"Value Error (likely config): {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         import traceback
#         traceback.print_exc()
