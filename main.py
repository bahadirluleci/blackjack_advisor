"""
Blackjack Game - Python Implementation

Author: Bahadir Lüleci
Date: 2025-02-27
Version: 0.2

Description:
---------------
This is a simple console-based Blackjack game implemented in Python.
The game follows standard Blackjack rules where the player competes
against the dealer (computer). The objective is to get a hand value
as close to 21 as possible without exceeding it.

Features:
---------------
- Uses an `Enum` class for card ranks and values.
- Implements a `Deck` class for shuffling and drawing cards.
- Supports Ace value adjustments (1 or 11).
- Player can `Hit` (draw a card) or `Stay` (end turn).
- Dealer automatically draws until at least 17.
- Determines the winner based on hand values.

Game Rules:
---------------
- Numbered cards (2-10) are worth their face value.
- Face cards (Jack, Queen, King) are worth 10 points.
- Aces can be worth 1 or 11, depending on the hand.
- If the player's total exceeds 21, they "Bust" and lose the game.
- The dealer wins if they have a higher valid score or the player busts.
- If both player and dealer have the same valid score, it's a "Draw".

How to Play:
---------------
1. The game starts by dealing two cards to both the player and the dealer.
2. The player can choose to "Hit" (take another card) or "Stay" (end their turn).
3. If the player busts (goes over 21), they lose immediately.
4. Once the player stays, the dealer reveals their hidden card and continues drawing until reaching at least 17.
5. The winner is determined based on the highest valid hand value.

To play, simply run the script and follow the on-screen prompts.

Enjoy the game!
"""

from game import GameBlackJack

if __name__ == "__main__":
    game = GameBlackJack()
    game.play()
