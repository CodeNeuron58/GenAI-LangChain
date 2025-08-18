from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

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

formatted_prompt_1 = promt_template_1.format(query="Black Hole")
result_1 = model.invoke(formatted_prompt_1)

formatted_prompt_2 = promt_template_2.format(text=result_1.content)
result_2 = model.invoke(formatted_prompt_2)

print(result_2.content)

