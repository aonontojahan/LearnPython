#pythom program to shuffle a deck of cards

import random
import itertools

deck = list(itertools.product(range(1, 14),['Hearts', 'Diamonds', 'Clubs', 'Spades']))
random.shuffle(deck)
print("Shuffled deck of cards:")

for card in range(5):
    print(deck[card][0], "of", deck[card][1])
    

