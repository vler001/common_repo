
from game import *

# Створення карти з її властивостями: масть, значення, що представляє, і значення, яке є результатом обчислення
class Card:
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value


if __name__ == '__main__':
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    suits_values = {"Spades": "\u2664", "Hearts": "\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
                            "Q": 10,
                            "K": 10}
    deck = []
# генеруємо колоду гральних карт
    for suit in suits:
        for card in cards:
            deck.append(Card(suits_values[suit], card, cards_values[card]))
    blackjack_game(deck)
