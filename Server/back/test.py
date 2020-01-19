from bot import Bot
import os, sys
b = Bot("Addy", debug=False)
first = True
#greeting = "How are you doing today?"

while not b.done:
    user = input(">> User: ")
    print(">> Bot: ", b.get_response(user))
