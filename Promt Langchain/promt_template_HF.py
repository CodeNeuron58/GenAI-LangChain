from langchain.prompts import PromptTemplate
from transformers.pipelines import pipeline
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint,HuggingFacePipeline
from langchain_huggingface.llms import HuggingFacePipeline

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Verify the Hugging Face API token
api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
if not api_token:
    raise ValueError("HUGGINGFACEHUB_ACCESS_TOKEN not found in .env file")

hf_pipeline = pipeline(
    "text-generation",
    model="EleutherAI/gpt-neo-2.7B",
    do_sample=True,
    min_length=50,
)

# Wrap in LangChain HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# Wrap that LLM with ChatHuggingFace for chat interface
chat_model = ChatHuggingFace(llm=llm)


template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name':'jit'})

response = chat_model.invoke(prompt)
print(response.content)



# need for download.
