# Task 5: Rule-Based AI Chatbot (if-elif, no ML)
from datetime import datetime

print("=== Rule-Based AI Chatbot === (type 'bye' to exit)")

while True:
    user = input("You: ").lower().strip()

    if user in ("hello", "hi", "hey"):
        print("Bot: Hello! Welcome.")
    elif "how are you" in user:
        print("Bot: I'm fine. Thanks for asking!")
    elif "your name" in user:
        print("Bot: I am AI-Bot, a simple rule-based chatbot.")
    elif "what is ai" in user:
        print("Bot: AI is the ability of machines to perform tasks that normally need human intelligence.")
    elif "what is python" in user:
        print("Bot: Python is a popular programming language used widely in AI and data science.")
    elif "time" in user:
        print("Bot: The time is", datetime.now().strftime("%I:%M %p"))
    elif "date" in user:
        print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))
    elif "help" in user:
        print("Bot: Try: hello, how are you, your name, what is ai, what is python, time, date, bye")
    elif user in ("bye", "exit", "quit"):
        print("Bot: Goodbye!")
        break
    elif user == "":
        print("Bot: Please type something.")
    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see what I can answer.")
