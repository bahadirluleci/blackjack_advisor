from deck import Deck
from hand import Hand
from strategy_table import HARD_STRATEGY, SOFT_STRATEGY, PAIR_STRATEGY, DEALER_UPCARD_MAPPING


class GameBlackJack:
    def __init__(self):
        self.deck = Deck(num_decks=6)
        print(len(self.deck.cards))
        self.human_hands = [Hand()]
        self.computer_hand = Hand()

    def show_hand(self, player_name, hand, hand_index=None):
        hand_label = f" Hand {hand_index + 1}" if hand_index is not None else ""
        print(f"\n{player_name}'s{hand_label} hand: \n{hand}")

    def check_winner(self, hand):
        human_score = hand.best_value()
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

    def get_best_move(self, player_hand):

        hand_values = [card.value for card in player_hand.cards]
        dealer_value = self.computer_hand.cards[0].value  # checks only first card

        num_aces = hand_values.count(11)

        total_value = sum(hand_values)

        while total_value > 21 and num_aces > 0:
            total_value -= 10  # refer ace as 1
            num_aces -= 1

        # if pair hand
        if len(player_hand.cards) == 2 and player_hand.cards[0].value == player_hand.cards[1].value:
            pair_value = player_hand.cards[0].value
            move = PAIR_STRATEGY.get(pair_value, {}).get(dealer_value, "S")  # if it is not in table return S

        # if soft hand (Ace)
        elif 11 in hand_values and sum(hand_values) <= 21:
            move = SOFT_STRATEGY.get(total_value, {}).get(dealer_value, "S")  # if it is not in table return S

        # if hard hand
        else:
            move = HARD_STRATEGY.get(total_value, {}).get(dealer_value, "S")  # if it is not in table return S

        print(DEALER_UPCARD_MAPPING[move])

    def player_turn(self):
        i = 0
        while i < len(self.human_hands):
            hand = self.human_hands[i]

            while True:
                self.show_hand("Player", hand, i)

                strategy = input("Do you want to learn the best move? (yes/no): ").strip().lower()
                if strategy == "yes":
                    self.get_best_move(hand)

                if hand.can_double():
                    choice = input("Do you want to Double? (yes/no): ").strip().lower()
                    if choice == "yes":
                        hand.can_hit = False
                        hand.add_card(self.deck.draw_card())

                if hand.can_split():
                    choice = input("Do you want to split? (yes/no): ").strip().lower()
                    if choice == "yes":
                        new_hand = Hand()

                        if hand.is_ace_split():
                            hand.can_hit = False
                            new_hand.can_hit = False

                        new_hand.add_card(hand.cards.pop())
                        new_hand.add_card(self.deck.draw_card())
                        hand.add_card(self.deck.draw_card())
                        self.human_hands.append(new_hand)
                        continue  # Restart loop for the split hand

                if hand.is_hand_value_21():
                    print("You have 21! No more moves needed.")
                    break

                # Ace split or double position
                if not hand.can_hit:
                    break

                move = input("Hit or Stand? ").strip().lower()
                if move == "hit":
                    hand.add_card(self.deck.draw_card())
                    if hand.is_busted():
                        print("Player busted!")
                        break
                    elif hand.is_hand_value_21():
                        print("You have 21! No more moves needed.")
                        break
                else:
                    print("You chose to Stand.")
                    break
            i += 1  # Move to the next hand

    def dealer_turn(self):
        while self.computer_hand.best_value() is None or self.computer_hand.best_value() < 17:
            self.computer_hand.add_card(self.deck.draw_card())
            if self.computer_hand.is_busted():
                print("Dealer busted! Player wins!")
                self.show_hand("Dealer", self.computer_hand)
                return

    def end_game_calculation(self):
        print("Turns Completed! Let's check hands")
        # case blackjack
        if len(self.human_hands) == 1:
            if self.human_hands[0].is_hand_blackjack() and not self.computer_hand.is_hand_blackjack():
                print("Player wins with BLACKJACK!")
                self.show_hand("Player", self.human_hands[0])
                self.show_hand("Dealer", self.computer_hand)
                return
            elif not self.human_hands[0].is_hand_blackjack() and self.computer_hand.is_hand_blackjack():
                print("Dealer wins with BLACKJACK!")
                self.show_hand("Player", self.human_hands[0])
                self.show_hand("Dealer", self.computer_hand)
                return

        # value calculation
        for hand_index, hand in enumerate(self.human_hands):
            self.show_hand("Player", hand, hand_index)
            print(f"Final Hand {hand_index + 1} values: {hand.calculate_values()} -> {hand.best_value()}")

        self.show_hand("Dealer", self.computer_hand)
        print(f"Final Dealer hand values: {self.computer_hand.calculate_values()} -> {self.computer_hand.best_value()}")

        for hand in self.human_hands:
            self.check_winner(hand)

    def play(self):
        # Initial hands
        for _ in range(2):
            self.human_hands[0].add_card(self.deck.draw_card())
            self.computer_hand.add_card(self.deck.draw_card())

        self.show_hand("Player", self.human_hands[0])
        print(f"Dealer's hand: \n{self.computer_hand.__str__(hide_second_card=True)}")

        # Player's turn (with splitting)
        if self.human_hands[0].is_hand_blackjack():
            print('BLACKJACK!')
        else:
            self.player_turn()

        # Dealer's turn
        self.dealer_turn()

        # Final Table
        self.end_game_calculation()
