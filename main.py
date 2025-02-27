from enum import Enum
import random

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')


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


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank.name
        self.value = rank.value

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in Ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop(0) if self.cards else None


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if card:
            self.cards.append(card)

    def __str__(self):
        return " || ".join(str(card) for card in self.cards)

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


class GameBlackJack:
    def __init__(self):
        self.deck = Deck()
        self.human_hand = Hand()
        self.computer_hand = Hand()

    def show_hand(self, player_name, hand):
        print(f"\n{player_name}'s hand: {hand}")

    def check_winner(self):
        human_score = self.human_hand.best_value()
        computer_score = self.computer_hand.best_value()

        if computer_score is None:
            print("Dealer busted! Player wins!")
        elif human_score is None:
            print("Player busted! Dealer wins!")
        elif human_score > computer_score:
            print("Player wins!")
        elif computer_score > human_score:
            print("Dealer wins!")
        else:
            print("It's a draw!")

    def play(self):
        # Initial hands
        for _ in range(2):
            self.human_hand.add_card(self.deck.draw_card())
            self.computer_hand.add_card(self.deck.draw_card())

        self.show_hand("Player", self.human_hand)
        self.show_hand("Dealer", self.computer_hand)

        # Player's turn
        while True:
            if input("\nHit or Stay? ").strip().lower() != "hit":
                print("You chose to stay.")
                break

            self.human_hand.add_card(self.deck.draw_card())
            self.show_hand("Player", self.human_hand)

            if self.human_hand.is_busted():
                print("Player busted! Dealer wins!")
                return

        # Dealer's turn
        while self.computer_hand.best_value() is None or self.computer_hand.best_value() < 17:
            self.computer_hand.add_card(self.deck.draw_card())
            self.show_hand("Dealer", self.computer_hand)

            if self.computer_hand.is_busted():
                print("Dealer busted! Player wins!")
                return

        # Final score check
        print(f"\nFinal Player hand values: {self.human_hand.calculate_values()}")
        print(f"Final Dealer hand values: {self.computer_hand.calculate_values()}")
        self.check_winner()


if __name__ == "__main__":
    game = GameBlackJack()
    game.play()
