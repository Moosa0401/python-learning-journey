"""
An accessable code that has been written by someone and we can use it

Reference: https://docs.python.org/3/library/random.html#module-random
"""
# load the content of a module
import random

#from-> A keyword to use specific function in a module
from random import choice

def main():
    #random.choice
    coin = random.choice(["heads", "tails"])
    coin2 = choice(["heads", "tails"])
    print(coin)
    print(coin2)

    #random.randint()
    number = random.randint(1,10) #inclusive
    print(number)

    #shuffle
    cards = ["jack", "queen", "king"]
    random.shuffle(cards)

    for card in cards:
        print(card)



main()