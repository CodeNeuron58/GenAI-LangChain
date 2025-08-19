from itertools import chain
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser

from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableParallel, RunnableLambda,RunnableBranch



from dotenv import load_dotenv
import os

from langchain_openai.llms import base

load_dotenv()

api_token = os.getenv("OPEN_ROUTER_API_KEY")
if not api_token:
    raise ValueError("OPEN_ROUTER_API_KEY not found in .env file")

class feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

# model = ChatOpenAI(
#     # model_name="meta-llama/llama-3.1-405b-instruct:free",
#     model_name = "microsoft/mai-ds-r1:free",
#     openai_api_key=api_token
# )

model = ChatOllama(
    model="llama3.1"
)

parser_1 = StrOutputParser()

parser_2 = PydanticOutputParser(pydantic_object=feedback)

promt_1 = PromptTemplate(
    template='Give the sentiment of the following feedback \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser_2.get_format_instructions()}

)

classifier_chain = promt_1 | model | parser_2


result = classifier_chain.invoke({'feedback': 'I hate this product'})

# print(result.sentiment)

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser_1),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser_1),
    RunnableLambda(lambda x: "could not find sentiment")
)

final_chain = classifier_chain | chain

result = final_chain.invoke({'feedback': 'I hate this product'})

print(result)



