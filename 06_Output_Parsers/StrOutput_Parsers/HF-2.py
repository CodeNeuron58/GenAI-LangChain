from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface.llms import HuggingFaceEndpoint
from dotenv import load_dotenv
import os



load_dotenv()

# String Output Parser
# This parser is used to extract the generated text from the model's output.
# It is useful when you want to get the raw text output from the model.
api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
if not api_token:
    raise ValueError("HUGGINGFACEHUB_ACCESS_TOKEN not found in .env file")

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=api_token
)

model = ChatHuggingFace(llm=llm)

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