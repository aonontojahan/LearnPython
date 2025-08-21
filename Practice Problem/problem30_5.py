# Python program to shuffle a deck of card

import random
import itertools

total_cards = list(itertools.product(range(1, 14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))
random.shuffle(total_cards)
print("Shuffled deck of cards:")

for card in range(5):
    print(total_cards[card][0], "of", total_cards[card][1])