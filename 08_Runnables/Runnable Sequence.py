# Import necessary libraries and modules from langchain and dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence
import os

# Load environment variables from .env file (useful for API keys, etc.)
load_dotenv()

load_dotenv()
api_token = os.getenv("OPEN_ROUTER_API_KEY")
if not api_token:
    raise ValueError("OPEN_ROUTER_API_KEY not found in .env file")

# Define a prompt template to generate a joke about a given topic
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',  # Template for generating a joke
    input_variables=['topic']  # The placeholder for the topic
)

# Initialize the OpenAI model for text generation
model = ChatOpenAI()

# Initialize the output parser to convert model outputs to strings
parser = StrOutputParser()

# Define a prompt template to explain the generated joke
prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',  # Template for explaining the joke
    input_variables=['text']  # The placeholder for the joke text
)

# Create the sequence of tasks using the | operator instead of RunnableSequence
# The | operator chains the tasks together, similar to how RunnableSequence works.
chain = prompt1 | model | parser | prompt2 | model | parser

# Execute the chain with the input topic 'AI'
print(chain.invoke({'topic': 'AI'}))

