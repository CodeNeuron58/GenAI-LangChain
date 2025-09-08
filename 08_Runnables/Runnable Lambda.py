# Import necessary libraries and modules from langchain and dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel
import os

# Load environment variables from .env file
load_dotenv()
api_token = os.getenv("OPEN_ROUTER_API_KEY")
if not api_token:
    raise ValueError("OPEN_ROUTER_API_KEY not found in .env file")

# Define a function for word count calculation
def word_count(text):
    """Function to count the number of words in a given text"""
    return len(text.split())

# Define a prompt template for generating a joke about a given topic
prompt = PromptTemplate(
    template='Write a joke about {topic}',  # Template for the joke
    input_variables=['topic']  # Variable to inject into the template (topic)
)

# Initialize the OpenAI model (can be used to generate the joke)
model = ChatOpenAI(
    # model_name="meta-llama/llama-3.1-405b-instruct:free",
    model_name = "mistralai/mistral-7b-instruct:free",
    # model_name = "tngtech/deepseek-r1t2-chimera:free",
    # model_name = "deepseek/deepseek-r1-0528:free",

    openai_api_key=api_token
)

# Initialize the output parser to interpret the output as a string
parser = StrOutputParser()

# Create a chain to generate the joke: use the prompt, model, and parser
joke_gen_chain = RunnableSequence(prompt, model, parser)

# Create a parallel chain that includes two tasks:
# - One task passes the joke through as-is (RunnablePassthrough)
# - Another task calculates the word count using a custom function (RunnableLambda)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),  # Pass the joke through without modification
    'word_count': RunnableLambda(word_count)  # Apply the word_count function to the joke
})

# Combine the joke generation chain and the parallel tasks (joke and word count)
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# Execute the final chain with the input topic 'AI'
result = final_chain.invoke({'topic': 'AI'})

# Format and print the result: the generated joke and its word count
final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)
