from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env (e.g., OPENAI_API_KEY)
load_dotenv()

# Initialize the ChatOpenAI agent using GPT‑4
# This uses the /chat/completions endpoint with a conversational context
model = ChatOpenAI(model="gpt‑4", temperature=0.0, max_completion_tokens= 10)

# This temperature determines randomness or you can say creativity

# Invoke the model with a user prompt to get a chat response
# We pass a single string—LangChain constructs it internally as a HumanMessage
result = model.invoke("What are the 7 continents?")

# Print the raw response object (useful for debugging metadata or tool traces)
print(result)

# Print the actual answer string from the response
print(result.content)
