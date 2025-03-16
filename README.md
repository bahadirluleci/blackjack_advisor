# Blackjack Game Documentation

## Overview
This project is a **console-based Blackjack game** implemented in Python. It assists players by providing suggestions for optimal moves during the game. The player competes against the dealer (computer) with the goal of reaching a hand value closest to 21 without exceeding it. The game includes features such as hand splitting, doubling down, and using strategies for different types of hands (pair, soft, and hard hands) to guide the player in making the best decisions.

---

## Files Structure
| File         | Description |
|-------------|------------|
| `card.py`   | Defines the `Card` class, representing individual playing cards. |
| `deck.py`   | Implements the `Deck` class for handling card shuffling and drawing. |
| `hand.py`   | Manages the player's and dealer's hands, including game rules like splitting, doubling, and busting. |
| `strategy_table.py`   | Keeps the European Blackjack Strategy table |
| `game.py`   | Contains the core game logic, including player and dealer turns. |
| `main.py`   | The entry point for running the game. |
| `README.md` | Documentation and instructions for using the game. |

---

## Classes and Methods
### `card.py`
#### **Class `Card`**
```python
class Card:
    def __init__(self, suit, rank):
```
- **Description**: Represents a playing card with a suit and rank.
- **Parameters**:
  - `suit` (str): The suit of the card (Hearts, Diamonds, Clubs, Spades).
  - `rank` (str): The rank of the card (Two, Three, ..., Ace).
- **Attributes**:
  - `value` (int): The numeric value of the card (e.g., 10 for King, 11 for Ace).


### `deck.py`
#### **Class `Deck`**
```python
class Deck:
    def __init__(self, num_decks=1)
```
- **Description**: Represents a deck of cards.
- **Parameters**:
  - `num_decks` (int): Number of decks to use (default: 1).
- **Methods**:
  - `shuffle()`: Shuffles the deck.
  - `draw_card() -> Card`: Draws a card from the deck.


### `hand.py`
#### **Class `Hand`**
```python
class Hand:
    def __init__(self)
```
- **Description**: Represents a player's or dealer's hand.
- **Methods**:
  - `add_card(card: Card)`: Adds a card to the hand.
  - `calculate_values() -> list[int]`: Calculates all possible hand values.
  - `best_value() -> int or None`: Returns the best hand value without busting.
  - `is_busted() -> bool`: Checks if the hand is over 21.
  - `can_split() -> bool`: Checks if the hand can be split.
  - `is_blackjack() -> bool`: Checks if the hand is a blackjack.


### `game.py`
#### **Class `GameBlackJack`**
```python
class GameBlackJack:
    def __init__(self)
```
- **Description**: Manages the Blackjack game.
- **Methods**:
  - `show_hand(player_name, hand, hand_index=None)`: Displays the player's hand.
  - `player_turn()`: Handles the player's turn.
  - `dealer_turn()`: Manages the dealer's automatic moves.
  - `check_winner(hand: Hand)`: Determines the winner.
  - `get_best_move(player_hand: Hand)`: provides the player with the best move to make during their turn based on their current hand and the dealer's upcard
  - `end_game_calculation()`: Displays the final game result.
  - `play()`: Starts and runs the game.


### `main.py`
#### **Game Execution**
```python
if __name__ == "__main__":
    game = GameBlackJack()
    game.play()
```
- **Description**: Runs the game when executed.

---

## How to Play
1. Run `main.py` to start the game.
2. The game deals two cards to both the player and the dealer.
3. The player can:
   - **Hit**: Draw another card.
   - **Stay**: End their turn.
   - **Double**: Double the bet and take only one more card (if eligible).
   - **Split**: If the first two cards are the same, split into two hands.
4. The dealer plays after the player.
5. The winner is determined based on the best hand value.

---
## Rules 
1. S17: Dealer stands on 17 or more.
2. Double: You can usually double on any 2 starting cards, although some tables permit only hands worth 9, 10 or 11
3. Split: You can split any 2 cards of the same value. Only 1 additional card on split Aces. A split Ace + 10 counts as 21, not Blackjack

---

## Future Improvements
- Add a graphical user interface (GUI).
- User will be informed about the best move


---

## Author
**Bahadir Lüleci**
- **Date**: 2025-03-16
- **Version**: 1.0

Enjoy the game!

