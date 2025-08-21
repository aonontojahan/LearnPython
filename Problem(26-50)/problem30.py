# Python program to shuffle a deck of card

import itertools
import random
deck = list(itertools.product(range(1, 14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))
random.shuffle(deck)
print("The shuffled deck of cards is:")
for card in range(5):
    print(deck[card][0], "of", deck[card][1])

    
