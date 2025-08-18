from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
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

parser = JsonOutputParser()

template = prompt_template = PromptTemplate(
    template='Give me the name , age and city of a fictional character \n {format_instructions}',
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

promt = template.format()

# print(promt)
result = model.invoke(promt)
# print(result)

final_result = parser.parse(result.content)
print(final_result)
print(type(final_result))

print(final_result['name'])
print(final_result['age'])
print(final_result['city'])




