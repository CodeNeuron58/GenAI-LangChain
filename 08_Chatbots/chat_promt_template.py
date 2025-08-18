from langchain_ollama import ChatOllama
# from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model="llama3.1")

# chat_template = ChatPromptTemplate([
#     SystemMessage(content="you are a helpful {domain} expert"),
#     HumanMessage(content = "Explain me in simple terms , what is {Topic}")
# ])


chat_template = ChatPromptTemplate([
    ("system","you are a helpful {domain} expert"),
    ("human","Explain me in simple terms , what is {Topic}")
])

formatted_prompt = chat_template.format_messages(domain="health", Topic="corona virus")

print(formatted_prompt)

result = model.invoke(formatted_prompt)
print(result.content)