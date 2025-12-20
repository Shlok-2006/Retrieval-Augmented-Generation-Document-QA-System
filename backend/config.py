import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHUNK_SIZE = 400
CHUNK_OVERLAP = 80
TOP_K = 2
