# Import the necessary modules from Langchain
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Initialize the model. In this case, it's the "llama3.1" model using Ollama
model = ChatOllama(model="llama3.1")

# Define the chat prompt template, which defines the structure of the conversation
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),  # System message to set the context
    MessagesPlaceholder(variable_name='chat_history'),    # Placeholder for chat history (dynamic content)
    ('human', '{query}')  # Human message where we will insert the user query (e.g., 'Where is my refund?')
])

# Initialize an empty list to store the chat history
chat_history = []

# Load the chat history from a text file
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())  # Read each line of the chat history and add it to the list

# Print the loaded chat history for debugging purposes
print(chat_history)

# Create a prompt by invoking the chat template with the necessary variables
# Here, we pass the 'chat_history' loaded from the file and a query (user's question)
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund'})

# Print the generated prompt to check its content
print(prompt)
