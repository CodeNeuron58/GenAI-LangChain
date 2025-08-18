from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.1")
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
