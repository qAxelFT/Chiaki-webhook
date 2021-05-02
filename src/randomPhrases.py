import random
import sys


def phrase():
    with open(f"{sys.path[0]}/assets/phrases.txt", "r") as file:    # Open the phrases list
        phrases = file.readlines()

    return phrases[random.randint(0, len(phrases)-1)]       # Return a random phrase from the list
