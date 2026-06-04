print("🤖 ChatBot Started!")
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is CodeAlpha Bot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
