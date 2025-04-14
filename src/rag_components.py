"""
Functions for initializing and configuring the RAG components.

Sets up:
- Embedding model (VertexAIEmbeddings - Step 5).
- Prompt template and context formatting (Step 8).
- Language model (ChatVertexAI - Step 9).

Based on guide.md steps 5, 8, and 9.
Vector store (Step 6) and Retriever (Step 7) instantiation happens in main.py
as they depend on the processed data (chunks).
"""
import logging
from langchain_google_vertexai import VertexAIEmbeddings, ChatVertexAI
from langchain_core.prompts import ChatPromptTemplate
from src import config # Import the config module

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Step 5: Instantiate Embedding Model ---
def get_embedding_model():
    """Initializes and returns the Vertex AI embedding model."""
    try:
        embeddings_model = VertexAIEmbeddings(
            model_name=config.EMBEDDING_MODEL_NAME,
            project=config.GOOGLE_CLOUD_PROJECT # Recommended to specify project
        )
        logging.info(f"Initialized embedding model: {embeddings_model.model_name}")
        return embeddings_model
    except Exception as e:
        logging.error(f"Error initializing embedding model: {e}")
        raise

# --- Step 8: Define Context Formatting & Prompt Template ---

def format_docs_with_metadata(docs):
    """Formats retrieved documents including metadata for the prompt."""
    formatted_docs = []
    for i, doc in enumerate(docs):
        # Prepare metadata strings with fallbacks
        relative_path = doc.metadata.get('relative_path', doc.metadata.get('source', 'Unknown Source'))
        links = doc.metadata.get('obsidian_links', [])
        if links:
            link_str = ", ".join(f"[[{link}]]" for link in links)
        else:
            link_str = "None"

        # Assemble the formatted string for this document
        doc_string = f"--- Context Document {i+1} ---\n"
        doc_string += f"Source File: {relative_path}\n"
        doc_string += f"Mentioned Links: {link_str}\n\n"
        doc_string += doc.page_content
        formatted_docs.append(doc_string)
    # Combine all formatted document strings
    logging.debug(f"Formatted {len(docs)} documents for context.")
    return "\n\n".join(formatted_docs)

# Define the prompt structure for Gemini
# Making this a function allows potential customization later if needed
def get_prompt_template():
    """Creates and returns the ChatPromptTemplate."""
    template = """You are an assistant specialized in answering questions about a specific project, based *only* on the provided context documents from an Obsidian vault.
Your task is to synthesize the information found in the context to answer the user's question accurately.
Pay close attention to the source file path and mentioned internal links provided for each context document, as they might indicate relationships between notes.
If the context does not contain the answer, state that clearly. Do not make up information.

Context:
{context}

Question: {question}

Answer:"""
    prompt = ChatPromptTemplate.from_template(template)
    logging.info("Prompt template created.")
    return prompt

# --- Step 9: Instantiate LLM (Gemini via Vertex AI) ---
def get_llm():
    """Initializes and returns the ChatVertexAI LLM."""
    try:
        llm = ChatVertexAI(
            model_name=config.LLM_MODEL_NAME,
            temperature=0.2, # Consider making temperature configurable too (e.g., config.LLM_TEMPERATURE)
            project=config.GOOGLE_CLOUD_PROJECT, # Recommended to specify project
            # You can add other parameters like max_output_tokens if needed
        )
        logging.info(f"Initialized LLM: {llm.model_name}")
        return llm
    except Exception as e:
        logging.error(f"Error initializing LLM: {e}")
        raise

# Example of how components might be retrieved (optional, useful for testing this module)
# if __name__ == '__main__':
#     print("Testing component initialization...")
#     try:
#         if not config.GOOGLE_CLOUD_PROJECT:
#             print("Error: GOOGLE_CLOUD_PROJECT not set. Cannot initialize Vertex AI components.")
#         else:
#             print(f"Using GCP Project: {config.GOOGLE_CLOUD_PROJECT}")
#             embeddings = get_embedding_model()
#             print(f"Embedding model: {embeddings.model_name}")
#             llm = get_llm()
#             print(f"LLM: {llm.model_name}")
#             prompt_template = get_prompt_template()
#             print("Prompt template retrieved.")
#             print("\nComponents seem to initialize okay (basic check).")
#     except Exception as e:
#         print(f"An error occurred during testing: {e}")

