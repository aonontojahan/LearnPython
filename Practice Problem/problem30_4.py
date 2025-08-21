# Python program to shuffle a deck of card
import random
import itertools

allcards = list(itertools.product(range(1, 14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))
random.shuffle(allcards)
print("Shuffled deck of cards:")

for card in range(5):
    print(allcards[card][0], "of", allcards[card][1])