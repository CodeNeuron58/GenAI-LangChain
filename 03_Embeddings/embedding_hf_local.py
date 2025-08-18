# Import HuggingFaceEmbeddings from LangChain's HuggingFace integration
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize the embedding model using a Sentence-Transformers model from Hugging Face
# 'all-MiniLM-L6-v2' is a lightweight, high-speed model ideal for semantic similarity and search
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Define a list of text documents to embed
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# Generate dense vector embeddings for each document
# Output: List of embedding vectors, one for each input string
vector = embedding.embed_documents(documents)

# Print the result (list of vectors) as a string
print(str(vector))
