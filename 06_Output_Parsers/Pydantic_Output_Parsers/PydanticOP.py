from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate, prompt
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

from langchain_huggingface.llms import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
if not api_token:
    raise ValueError("HUGGINGFACEHUB_ACCESS_TOKEN not found in .env file")

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=api_token
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt = 18 , description="Age of the person")
    city: str = Field(description="City of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="generate the name , age , and city of a fictional {place} person.\n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.invoke({"place":"indian"})
# print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)
print(final_result.name)
print(final_result.age)
print(final_result.city)



