# Import the OpenAI class from langchain_openai package
from langchain_openai import OpenAI

# Import function to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables (e.g., OpenAI API key) from a .env file into the environment
load_dotenv()

# Initialize the OpenAI LLM instance
# You can specify different models like "gpt-3.5-turbo-instruct", "text-davinci-003", etc.
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# Call the model with a prompt and store the result
# This will send the prompt to the OpenAI API and get a response
result = llm.invoke("write text here ?")  # Replace with your actual prompt

# Print the result returned by the model
print(result)
