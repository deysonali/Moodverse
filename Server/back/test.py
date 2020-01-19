from bot import Bot
import os, sys
b = Bot("addy")
first = True
greeting = "How are you doing today?"

while not b.done:
    if first:
        user = input(" >>" + greeting + " ")
    else:
        user = input(">> User")
    print(">> Bot", b.get_response(user))
