from deck import Deck
from hand import Hand


class GameBlackJack:
    def __init__(self):
        self.deck = Deck()
        self.human_hand = Hand()
        self.computer_hand = Hand()

    def show_hand(self, player_name, hand):
        print(f"\n{player_name}'s hand: \n{hand}")

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
            self.show_hand("Dealer", self.computer_hand)

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
