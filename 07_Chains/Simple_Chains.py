from itertools import chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv("OPEN_ROUTER_API_KEY")
if not api_token:
    raise ValueError("OPEN_ROUTER_API_KEY not found in .env file")

model = ChatOpenAI(
    # model_name="meta-llama/llama-3.1-405b-instruct:free",
    model_name = "mistralai/mistral-7b-instruct:free",
    openai_api_key=api_token
)

prompt = PromptTemplate(
    input_variables=['query'],
    template='Write  5 interesting facts about {query}'
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"query": "Black Hole"})
print(result)





