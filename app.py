import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    # Patterns for greeting the chatbot
    ['hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']],
    ['how are you', ['I am good, thanks for asking! How can I help you today?']],
    
    # Patterns for asking about the chatbot's purpose
    ['what is your purpose', ['I am here to assist and answer your questions!']],
    ['why are you here', ['I am here to help you with any questions you have!']],
    
    # Patterns for asking for help
    ['help', ['Sure, what do you need help with?']],
    ['how do I', ['I can help you with that! What do you need help with?']],
    
    # Default response
    ['(.*)', ["I'm sorry, I don't understand. Can you please rephrase your question?"]],
]

# Define a function to chat with the user
def chat():
    print("Hi! I am your personal chatbot. How can I assist you today?")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == '__main__':
    chat()
