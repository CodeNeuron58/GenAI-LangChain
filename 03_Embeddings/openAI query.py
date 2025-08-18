# Import the OpenAIEmbeddings class from LangChain's OpenAI integration
from langchain_openai import OpenAIEmbeddings

# Load environment variables from a .env file (e.g., your OpenAI API key)
from dotenv import load_dotenv
load_dotenv()

# Initialize the OpenAI embedding model
# - 'text-embedding-3-large' is a high-performance embedding model
# - 'dimensions=32' downsamples the default embedding size to 32 dimensions (trade-off: less accuracy, more speed)
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

# Generate a vector embedding for a given input query
result = embedding.embed_query("Delhi is the capital of India")

# Print the resulting embedding vector as a string
print(str(result))