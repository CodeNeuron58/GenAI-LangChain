# Import necessary libraries and modules from langchain and dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel
import os

# Load environment variables from .env file (like API keys, etc.)
load_dotenv()

load_dotenv()
api_token = os.getenv("OPEN_ROUTER_API_KEY")
if not api_token:
    raise ValueError("OPEN_ROUTER_API_KEY not found in .env file")

# Define a prompt template for generating a tweet about a topic
prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',  # Template for tweet generation
    input_variables=['topic']  # The variable to insert into the template
)

# Define a prompt template for generating a LinkedIn post about a topic
prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',  # Template for LinkedIn post generation
    input_variables=['topic']  # The variable to insert into the template
)

# Initialize the OpenAI model (to generate text based on the prompts)
model = ChatOpenAI()

# Initialize the output parser to interpret the generated text as a string
parser = StrOutputParser()

# Define a parallel chain where both tasks (tweet and LinkedIn post) run at the same time
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),  # Chain for generating the tweet
    'linkedin': RunnableSequence(prompt2, model, parser)  # Chain for generating the LinkedIn post
})

# Invoke the parallel chain with the topic 'AI'
result = parallel_chain.invoke({'topic': 'AI'})

# Print the results: tweet and LinkedIn post
print(result['tweet'])
print(result['linkedin'])
