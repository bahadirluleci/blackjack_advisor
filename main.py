from enum import Enum
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')


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
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in suits for rank in Ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_one(self):
        return self.cards.pop(0)


def hand_value_calculation(hand):
    values = [0]
    for card in hand:
        if card.rank == Ranks.ACE.name:
            for i in range(len(values)):
                old_val = values[i]
                values[i] += Ranks.ACE.value
                values.append(old_val + 1)
        else:
            if len(values):
                for i in range(len(values)):
                    values[i] += card.value

    return values


class GameBlackJack:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.human_hand = []
        self.computer_hand = []

        self.human_hand_calculation = []
        self.computer_hand_calculation = []

    def show_hand(self, who):
        print()
        if who == 'user':
            print('User hand')
            for i in range(len(self.human_hand)):
                print(f'{self.human_hand[i]} || ', end=" ")
            print('\n')
        else:
            print('Dealer hand')
            for i in range(len(self.computer_hand)):
                print(f'{self.computer_hand[i]} || ', end=" ")

    def check_winner(self):
        max_valid_human = max((num for num in self.human_hand_calculation if num <= 21), default=None)
        max_valid_comp = max((num for num in self.computer_hand_calculation if num <= 21), default=None)
        if max_valid_comp is None:
            print('Dealer busted! Player wins!')
            return
        if max_valid_human is None:
            print('Player busted! Dealer wins!')
            return
        if max_valid_human > max_valid_comp:
            print('Player wins!')
            return
        elif max_valid_comp > max_valid_human:
            print('Dealer wins!')
            return
        else:
            print('Draw')

    def play(self):
        for i in range(2):
            self.human_hand.append(self.deck.remove_one())
            self.computer_hand.append(self.deck.remove_one())
        self.show_hand('user')
        self.show_hand('dealer')

        while True:
            if input('\nHit or Stay ?').lower() != 'hit':
                print('Goodbye!')
                break

            self.human_hand.append(self.deck.remove_one())
            self.human_hand_calculation = hand_value_calculation(self.human_hand)
            if max((num for num in self.human_hand_calculation if num <= 21), default=None) is None:
                print('Player busted! Dealer wins!')
                return

            self.show_hand('user')
            if max((num for num in self.human_hand_calculation if 17 <= num <= 21), default=None) is not None:
                self.computer_hand_calculation = hand_value_calculation(self.computer_hand)
                self.show_hand('dealer')
                break

            self.computer_hand.append(self.deck.remove_one())
            self.computer_hand_calculation = hand_value_calculation(self.computer_hand)
            if max((num for num in self.human_hand_calculation if num <= 21), default=None) is None:
                print('Dealer busted! Player wins!')
                return
            self.show_hand('dealer')


        print(f'Player hand: {self.human_hand_calculation}')
        print(f'Dealer hand: {self.computer_hand_calculation}')
        self.check_winner()


if __name__ == '__main__':
    game = GameBlackJack()
    game.play()
