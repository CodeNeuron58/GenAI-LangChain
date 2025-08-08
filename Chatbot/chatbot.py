# Importing required classes from langchain_ollama and langchain_core
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

# Initializing the ChatOllama model with a specific version (llama3.1 in this case)
model = ChatOllama(model="llama3.1")

# Prompting the user for the system message, which will guide the model's behavior
system_message = input("System_msg : ")

# Initializing the chat history list with the system message
# The SystemMessage serves as the initial instruction to the model
chat_history: list = [
    SystemMessage(content=system_message)
]

# Entering an infinite loop where the user can continuously interact with the model
while True:
    # Getting the user's input (message) in the conversation
    user_input = input("You : ")

    # Append the user's message to the chat history
    chat_history.append(HumanMessage(content=user_input)) 

    # If the user types 'exit', break the loop and end the conversation
    if user_input.lower() == "exit":
        break 

    # Use the model to generate a response based on the chat history
    result = model.invoke(chat_history)

    # Append the model's response (AIMessage) to the chat history
    chat_history.append(AIMessage(content=result.content))

    # Print the AI's response to the user
    print("AI: ", result.content)

# After the loop is exited, print the entire conversation history
# This includes both the user inputs and the AI responses
print(chat_history)

