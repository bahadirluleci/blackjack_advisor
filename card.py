from enum import Enum


class Ranks(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11


VISUALIZATION = {Ranks.TWO.name: '2', Ranks.THREE.name: '3', Ranks.FOUR.name: '4', Ranks.FIVE.name: '5',
                 Ranks.SIX.name: '6', Ranks.SEVEN.name: '7', Ranks.EIGHT.name: '8', Ranks.NINE.name: '9',
                 Ranks.TEN.name: '10', Ranks.JACK.name: 'J', Ranks.QUEEN.name: 'Q', Ranks.KING.name: 'K',
                 Ranks.ACE.name: 'A'}

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank.name
        self.value = rank.value

    def __str__(self):
        return f"{self.rank} of {self.suit}"
