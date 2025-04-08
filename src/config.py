"""
Configuration settings for the RAG application.

Contains configuration variables like file paths and model names,
and loads sensitive information (API keys, project IDs) from the .env file.
Corresponds to parts of Step 1 (loading GOOGLE_CLOUD_PROJECT) and variables
used in Steps 2, 5, 6, and 9 from guide.md.
"""

# Example in src/config.py
import os
from dotenv import load_dotenv

load_dotenv() # Loads variables from .env into environment

GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")

if not GOOGLE_CLOUD_PROJECT:
    print("Warning: GOOGLE_CLOUD_PROJECT environment variable not set.")