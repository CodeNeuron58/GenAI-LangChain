# Import Ollama embeddings for generating vector representations of text
from langchain_ollama import OllamaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Ollama embeddings with llama2 model
# Note: Requires Ollama server running locally on port 11434
embedding = OllamaEmbeddings(
    model="llama3.1" 
)

# Sample cricket player descriptions for semantic search
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

# Search query to find relevant cricket player information
query = 'tell me about bumrah'

# Generate vector embeddings for all documents using Ollama
doc_embeddings = embedding.embed_documents(documents)

# Convert query to vector embedding
query_embedding = embedding.embed_query(query)

# Calculate similarity scores between query and documents using cosine similarity
scores = cosine_similarity([query_embedding], doc_embeddings)[0] # type: ignore

# Find document with highest similarity score
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

# Display results
print("Query:", query)
print("Most similar document:", documents[index])
print("Similarity score is:", score)