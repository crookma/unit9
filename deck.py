# By: Magnus Crooke, File Name: compare.py, Last modified: 11-17-17, This program created the cards in a deck.
import random

import card


class Deck:
    def __init__(self):
        """
        This function creates all of the cards in the deck.
        """
        self.deck = []
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        for suit in suits:
            for rank in range(1, 14):
                firstcard = card.Card(rank, suit)
                self.deck.append(firstcard)

    def shuffle(self):
        """
        This function creates a shuffled deck of cards.
        """
        random.shuffle(self.deck)

    def dealacard(self):
        """
        This function deals out the cards being played with.
        """
        newrange = len(self.deck)
        dealingcards = self.deck.pop(0)
        return dealingcards
