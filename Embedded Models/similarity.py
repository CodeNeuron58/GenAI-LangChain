# Import OpenAIEmbeddings for generating vector representations of text
from langchain_openai import OpenAIEmbeddings

# Load environment variables (like the OpenAI API key)
from dotenv import load_dotenv

# Import cosine similarity and NumPy for vector operations
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load .env file (must contain OPENAI_API_KEY)
load_dotenv()

# Initialize the OpenAI embedding model with reduced dimensionality (300)
# 'text-embedding-3-large' defaults to 1536 dimensions, but here we're downsampling to 300
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

# List of documents to embed
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# The input query for which we want to find the most semantically similar document
query = 'tell me about bumrah'

# Generate embeddings for the documents
doc_embeddings = embedding.embed_documents(documents)

# Generate embedding for the input query
query_embedding = embedding.embed_query(query)

# Compute cosine similarity between the query and each document
# Result is a list of similarity scores between query and each doc
scores = cosine_similarity([query_embedding], doc_embeddings)[0] # type: ignore

# Find the index of the document with the highest similarity score
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

# Print the matched document and its similarity score
print("Query:", query)
print("Most similar document:", documents[index])
print("Similarity score is:", score)