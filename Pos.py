import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt', quiet=True)

# Pairs for the chatbot (patterns and responses)
pairs = [
    (r"hello|hi|hey", ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]),
    (r"what is your name\?", ["I am a chatbot created for this PoC project.", "My name is Chatbot, your virtual assistant!"]),
    (r"how are you\?", ["I'm just a program, but I'm functioning perfectly. How about you?"]),
    (r"tell me a joke", ["Why did the scarecrow win an award? Because he was outstanding in his field!"]),
    (r"thank you|thanks", ["You're welcome!", "Happy to help!"]),
    (r"quit", ["Goodbye! Have a great day!", "See you next time!"]),
]

# Chatbot functionality
def chatbot_poc():
    print("Chatbot: Hello! I'm your PoC Chatbot. Type 'quit' to exit the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()
