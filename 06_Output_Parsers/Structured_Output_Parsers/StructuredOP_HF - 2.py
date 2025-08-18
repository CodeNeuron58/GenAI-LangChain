from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


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


schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me 3 facts about {topic}\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}

)

chains = template | model | parser

result = chains.invoke({"topic": "Cricket"})

print(result)
print(result["fact_1"])
print(result["fact_2"])
print(result["fact_3"])





# Limitations :
# 1. The model may not always generate the expected output format.
# 2. The model may not always generate the expected number of facts.
# 3. The model may not always generate the expected type of facts.
# 4. The model lack validation feature to ensure the generated output is in the expected format.
