from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Verify the Hugging Face API token
api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
if not api_token:
    raise ValueError("HUGGINGFACEHUB_ACCESS_TOKEN not found in .env file")

# # Option 1: Using repo_id (recommended)
llm = HuggingFaceEndpoint(
    model="HuggingFaceH4/zephyr-7b-beta",  # Chat-tuned model
    huggingfacehub_api_token=api_token
)

# Alternative Option 2: Using model parameter instead
# llm = HuggingFaceEndpoint(
#     repo_id="google/flan-t5-small",
#     huggingfacehub_api_token=api_token
# )

# Initialize the ChatHuggingFace model
model = ChatHuggingFace(llm=llm)

# Invoke the model
result = model.invoke("What is the capital of India?")
print(result.content)