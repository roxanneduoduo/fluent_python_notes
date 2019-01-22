from random import shuffle
from frenchdeck import FrenchDeck


deck = FrenchDeck()

try:
    shuffle(deck)
except TypeError as err:
    print('TypeError: {}'.format(err))


def set_card(deck, position, card):
    deck._cards[position] = card


# Monkey Patch
FrenchDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])
