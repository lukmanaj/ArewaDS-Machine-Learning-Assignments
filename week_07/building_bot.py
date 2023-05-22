# My humble attempt

import random

# This list contains the random responses
random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

def chat():
    print("Hello, I am Marvin, the simple robot.")
    print("You can end this conversation at any time by typing 'bye'")
    print("After typing each answer, press 'enter'")
    print("How are you today?")

    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":
            break
        else:
            response = random.choice(random_responses)
            print(response)

    print("It was nice talking to you, goodbye!")

if __name__ == "__main__":
    chat()
