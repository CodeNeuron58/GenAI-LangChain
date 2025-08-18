# Import OpenAIEmbeddings to generate embeddings using OpenAI's API
from langchain_openai import OpenAIEmbeddings

# Load environment variables, especially the OpenAI API key from a .env file
from dotenv import load_dotenv
load_dotenv()

# Initialize the embedding model with:
# - model: 'text-embedding-3-large' (OpenAI's high-performance embedding model)
# - dimensions: 32 (optional dimensionality reduction for faster computation; trade-off: lower embedding quality)
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# List of documents/sentences to be embedded
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Generate embeddings for each document in the list
# Returns a list of embedding vectors, one per document
result = embedding.embed_documents(documents)

# Print the list of vectors (each is a list of floats with 32 dimensions)
print(str(result))
