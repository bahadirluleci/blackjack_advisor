import random
from card import Card, SUITS, Ranks


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in Ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0) if self.cards else None
