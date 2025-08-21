# Python program to shuffle a deck of card

import random
import itertools

cards = list(itertools.product(range(1, 14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))
random.shuffle(cards)
print("Shuffled deck of cards:")

for card in range(5):
    print(cards[card][0], "of", cards[card][1])