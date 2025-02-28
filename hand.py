from card import Ranks, VISUALIZATION


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if card:
            self.cards.append(card)

    def __str__(self, hide_second_card=False):
        """ display with an option to hide the second card (dealer's first move) """
        lines = [""] * 5  # Store each row of ASCII card representation

        for i, card in enumerate(self.cards):
            if hide_second_card and i == 1:  # Hide the second card
                lines[0] += "┌─────┐  "
                lines[1] += "│░░░░░│  "
                lines[2] += "│░░░░░│  "
                lines[3] += "│░░░░░│  "
                lines[4] += "└─────┘  "
            else:
                rank = VISUALIZATION[card.rank]
                suit = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}[card.suit]  # Unicode symbols

                lines[0] += "┌─────┐  "
                lines[1] += f"│{rank:<2}   │  "  # Left-align rank
                lines[2] += f"│  {suit}  │  "
                lines[3] += f"│   {rank:>2}│  "  # Right-align rank
                lines[4] += "└─────┘  "

        return "\n".join(lines)  # Combine all rows

    def calculate_values(self):
        """Calculate possible hand values, considering Aces as 1 or 11."""
        values = [0]
        for card in self.cards:
            if card.rank == "ACE":
                values = [v + Ranks.ACE.value for v in values] + [v + 1 for v in values]
            else:
                values = [v + card.value for v in values]
        return values

    def best_value(self):
        """Return the highest hand value <= 21, otherwise return None (bust)."""
        return max((v for v in self.calculate_values() if v <= 21), default=None)

    def is_busted(self):
        return self.best_value() is None
