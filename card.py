# By: Magnus Crooke, File Name: compare.py, Last modified: 11-17-17, This program creates the cards in the deck.
class Card:
    def __init__(self, rank, suit):
        """
        This function assigning the suit and rank of cards.
        :param rank: This function is saving the rank of the card.
        :param suit: This function is saving the suit of the card.
        """
        self.rank = rank
        self.suit = suit

    def getSuit(self):
        """
        This function gets the suit of each card.
        """
        return self.suit

    def getRank(self):
        """
        This function gets the rank of each card.
        """
        return self.rank

    def __str__(self):
        """
        This function prints out the cards rank and suit.
        """
        return str(self.rank) + " of " + self.suit

