#Python proram to shuflle a deck of cards
import random
import itertools

box_of_cards = list(itertools.product(range(1, 14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))
random.shuffle(box_of_cards)
print("Shuffled deck of cards:")
for card in range(5):
    print(box_of_cards[card][0], "of", box_of_cards[card][1])