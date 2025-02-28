RANKS = {
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9,
    "TEN": 10,
    "JACK": 10,
    "QUEEN": 10,
    "KING": 10,
    "ACE": 11
}

VISUALIZATION = {
    "TWO": "2", "THREE": "3", "FOUR": "4", "FIVE": "5", "SIX": "6",
    "SEVEN": "7", "EIGHT": "8", "NINE": "9", "TEN": "10",
    "JACK": "J", "QUEEN": "Q", "KING": "K", "ACE": "A"
}

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')


class Card:
    """Represents a playing card with suit and rank."""
    def __init__(self, suit, rank):
        if rank not in RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        self.suit = suit
        self.rank = rank
        self.value = RANKS[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
