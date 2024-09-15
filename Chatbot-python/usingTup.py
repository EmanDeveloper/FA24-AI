def chatbot():
    responses = [
        (("hello", "hi"), "Hello! How can I help you today?"),
        (("how are you", "how's it going"), "I'm just a bot, but I'm doing great! How about you?"),
        (("what is your name", "who are you"), "I'm a simple chatbot created in Python."),
        (("bye", "goodbye"), "Goodbye! Have a great day!"),
        (("thanks", "thank you"), "You're welcome!"),
    ]

    print("Chatbot: Hi! I'm your basic Python chatbot. Ask me something!")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["exit", "quit"]:
            print("Chatbot: Exiting the chat. Goodbye!")
            break

        # Search for a matching response
        response_found = False
        for questions, response in responses:
            if any(keyword in user_input for keyword in questions):
                print(f"Chatbot: {response}")
                response_found = True
                break

        if not response_found:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
