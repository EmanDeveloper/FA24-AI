
def chatbot():
    responses = [
        {"question": ["hello", "hi"], "response": "Hello! How can I help you today?"},
        {"question": ["how are you", "how's it going"], "response": "I'm just a bot, but I'm doing great! How about you?"},
        {"question": ["what is your name", "who are you"], "response": "I'm a simple chatbot created in Python."},
        {"question": ["bye", "goodbye"], "response": "Goodbye! Have a great day!"},
        {"question": ["thanks", "thank you"], "response": "You're welcome!"},
    ]

    print("Chatbot: Hi! I'm your basic Python chatbot. Ask me something!")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["exit", "quit"]:
            print("Chatbot: Exiting the chat. Goodbye!")
            break

        # Search for a matching response
        response_found = False
        for item in responses:
            if any(keyword in user_input for keyword in item["question"]):
                print(f"Chatbot: {item['response']}")
                response_found = True
                break

        if not response_found:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
