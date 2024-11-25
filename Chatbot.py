# Simple chatbot using Python

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. How can I assist you?")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm Chatbot, your virtual assistant.")
        
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather right now, but you can try a weather app!")
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
  
