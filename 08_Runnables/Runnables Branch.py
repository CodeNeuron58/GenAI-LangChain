# Import necessary libraries and modules
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda
import os

# Load environment variables from .env file
load_dotenv()

load_dotenv()
api_token = os.getenv("OPEN_ROUTER_API_KEY")
if not api_token:
    raise ValueError("OPEN_ROUTER_API_KEY not found in .env file")

# Define a prompt template for generating a detailed report
prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',  # The template for the report
    input_variables=['topic']  # Variable to inject into the template
)

# Define a prompt template for summarizing a given text
prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',  # The template for summarizing text
    input_variables=['text']  # Variable to inject into the template
)

# Initialize the model (in this case, a language model from OpenAI)
model = ChatOpenAI(
    # model_name="meta-llama/llama-3.1-405b-instruct:free",
    model_name = "mistralai/mistral-7b-instruct:free",
    # model_name = "tngtech/deepseek-r1t2-chimera:free",
    # model_name = "deepseek/deepseek-r1-0528:free",

    openai_api_key=api_token
)

# Initialize the output parser (for string output parsing)
parser = StrOutputParser()

# Create the first chain for generating a report using the prompt1, model, and parser
report_gen_chain = prompt1 | model | parser

# Create a branching logic (RunnableBranch)
branch_chain = RunnableBranch(
    # This lambda function checks the length of the text (generated report) to decide which chain to execute
    (lambda x: len(x.split()) > 300,  # Condition: If the generated report is over 300 words
     prompt2 | model | parser),  # If the condition is true, summarize the report
    RunnablePassthrough()  # If the condition is false (report is under 300 words), do nothing (pass through)
)

# Final sequence of tasks: generate the report, then branch based on word count
final_chain = RunnableSequence(report_gen_chain, branch_chain)

# Execute the final chain, providing the topic as input
print(final_chain.invoke({'topic': 'Russia vs Ukraine'}))
