# Import OpenAIEmbeddings for generating vector representations of texts.
from langchain_huggingface import HuggingFaceEmbeddings

# Import cosine similarity and NumPy for vector operations
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initialize the HuggingFace embedding model
embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

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
scores = cosine_similarity(np.array([query_embedding]), np.array(doc_embeddings))[0]

# Find the index of the document with the highest similarity score
index = np.argmax(scores)
score = scores[index]

# Print the matched document and its similarity score
print("Query:", query)
print("Most similar document:", documents[index])
print(f"Similarity score is: {score:.4f}")
