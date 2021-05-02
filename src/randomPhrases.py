import random
import os


def phrase():
    with open(f"{os.getcwd()}/assets/phrases.txt", "r") as file:    # Open the phrases list
        phrases = file.readlines()

    return phrases[random.randint(0, len(phrases)-1)]       # Return a random phrase from the list
