import random
from card import Card, SUITS, RANKS


class Deck:

    def __init__(self, num_decks=1):  # Default: 1 deck
        """ Creates a deck with the specified number of decks """
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS] * num_decks
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0) if self.cards else None
