from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("chatbot")

convo = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
trainer = ListTrainer(chatbot)

response = chatbot.get_response("HI")
print(response)