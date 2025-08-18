from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os


load_dotenv()

# String Output Parser
# This parser is used to extract the generated text from the model's output.
# It is useful when you want to get the raw text output from the model.
api_token = os.getenv("OPEN_ROUTER_API_KEY")
if not api_token:
    raise ValueError("OPEN_ROUTER_API_KEY not found in .env file")

model = ChatOpenAI(
    # model_name="meta-llama/llama-3.1-405b-instruct:free",
    model_name = "mistralai/mistral-7b-instruct:free",
    openai_api_key=api_token
)


# For detailed report on any topic

promt_template_1 = PromptTemplate(
    input_variables=['query'],
    template='Write a detailed report on {query}'
)

# For summary of any topic

promt_template_2 = PromptTemplate(
    input_variables=['text'],
    template='Write a summary on {text}'
)

parsers = StrOutputParser()

chain = promt_template_1 | model | parsers | promt_template_2 | model | parsers

result = chain.invoke({"query": "Black Hole"})
print(result)