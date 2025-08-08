from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.1")

#this will create a list to hold the conversation . 
chat_history = []

while True :
    user_input = input("You : ")
    chat_history.append(user_input) # Everytime user ask something ,it will be added to the history . 
    if user_input == "exit":
        break 
    result = model.invoke(chat_history)  # since, chat_history contains user input ,model will use this for output. 
    chat_history.append(result)   # we need to save the ai output to history also . 
    print("AI: " ,result.content)
    
print(chat_history)  # the entire history will be here . 
    
