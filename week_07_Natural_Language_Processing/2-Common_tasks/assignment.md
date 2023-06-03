# Make a Bot talk back

## Instructions

In the past few lessons, you programmed a basic bot with whom to chat. This bot gives random answers until you say 'bye'. Can you make the answers a little less random, and trigger answers if you say specific things, like 'why' or 'how'? Think a bit how machine learning might make this type of work less manual as you extend your bot. You can use NLTK or TextBlob libraries to make your tasks easier.

## Solution

bot.py

```py
import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
import nltk

nltk.download('punkt')
extractor = ConllExtractor()

# Define a dictionary of trigger words and their corresponding responses

trigger_responses = {
"why": "I'm sorry, I'm just a simple bot and don't have the capacity to answer 'why' questions.",
"how": "I'm sorry, I'm not equipped to provide detailed explanations on 'how' things work.",
"bye": "Goodbye! It was nice chatting with you.",
}

def main():
    print("Hello, I am Marvin, the friendly robot.")
    print("You can end this conversation at any time by typing 'bye'")
    print("After typing each answer, press 'enter'")
    print("How are you today?")


    while True:
        user_input = input("> ")

        if user_input.lower() in trigger_responses:
        # If the user input matches a trigger word, provide the corresponding response
            print(trigger_responses[user_input.lower()])
            break
        elif user_input.lower() == "bye":
            print("Goodbye! It was nice chatting with you.")
            break
        else:
            user_input_blob = TextBlob(user_input, np_extractor=extractor)
            np = user_input_blob.noun_phrases
            response = ""

        if user_input_blob.polarity <= -0.5:
            response = "Oh dear, that sounds bad. "
        elif user_input_blob.polarity <= 0:
            response = "Hmm, that's not great. "
        elif user_input_blob.polarity <= 0.5:
            response = "Well, that sounds positive. "
        elif user_input_blob.polarity <= 1:
            response = "Wow, that sounds great. "

        if len(np) != 0:
            response += f"Can you tell me more about {np[0].pluralize()}?"
        else:
            response += "Can you tell me more?"
            
        print(response)
if name == "main":
main()

```
