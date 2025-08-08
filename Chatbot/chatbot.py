from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.1")

while True :
    user_input = input("You : ")
    if user_input == "exit":
        break 
    result = model.invoke(user_input)
    print("AI: " ,result.content)
    
