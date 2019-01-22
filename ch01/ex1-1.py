"""
>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')

"""

import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)




class FrenchDeck:
    """
    >>> deck = FrenchDeck()
    >>> len(deck)
    52

    >>> deck[0]
    Card(rank='2', suit='spades')
    >>> deck[-1]
    Card(rank='A', suit='hearts')

    >>> from random import choice
    >>> choice(deck)        # doctest: +ELLIPSIS
    >>> choice(deck)        # doctest: +ELLIPSIS
    >>> choice(deck)        # doctest: +ELLIPSIS

    >>> deck[:3]            # doctest: +ELLIPSIS
    >>> deck[12::13]        # doctest: +ELLIPSIS

    for card in deck:        # doctest: +ELLIPSIS
        print(card)

    >>> for card in reversed(deck):        # doctest: +ELLIPSIS
    ...     print(card)


    >>> Card('Q', 'hearts') in deck
    True
    >>> Card('7', 'beasts') in deck
    False

    >>> for card in sorted(deck, key=spades_high):        # doctest: +ELLIPSIS
    ...     print(card)
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
