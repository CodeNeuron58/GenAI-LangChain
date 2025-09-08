# Import necessary libraries and modules from langchain and dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
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

# Create a chain to generate the joke using the first prompt, model, and parser
joke_gen_chain = RunnableSequence(prompt1, model, parser)

# Create a parallel chain with two tasks:
# 1. Pass the joke through without any modification (RunnablePassthrough)
# 2. Explain the joke using the second prompt, model, and parser
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),  # This just passes the joke through unchanged
    'explanation': RunnableSequence(prompt2, model, parser)  # This generates the explanation
})

# Combine the joke generation chain and the parallel chain into a final sequence
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# Execute the final chain with the topic 'cricket'
print(final_chain.invoke({'topic': 'cricket'}))
