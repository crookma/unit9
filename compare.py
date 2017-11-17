# By: Magnus Crooke, File Name: compare.py, Last modified: 11-17-17, This program is a game of compare.
import card
import deck
newcard = card.Card(1, "Hearts")


def main():
    """
    This function plays the game of compare
    :return:
    """
    newdeck = deck.Deck()
    newdeck.shuffle()
    firstplayer_cards = []
    secondplayer_cards = []
    for x in range(5):
        firstplayer_cards.append(newdeck.dealacard())
        secondplayer_cards.append(newdeck.dealacard())
    playing_game(firstplayer_cards, secondplayer_cards)


def playing_game(firstplayer_cards, secondplayer_cards):
    """
    This function asks the user if they would like to play the game
    :param firstplayer_cards: This function keeps track of all of the points for the first player.
    :param secondplayer_cards: This function keeps track of all of the points for the second player.
    :return: This function returns who won the game, with how many points they had.
    """
    P1_score = 0
    P2_score = 0
    print("Press 'y' for yes, and 'n' for no")
    playgame = input("Would you like to play a game of compare?")
    if playgame == 'y':
        for x in range(len(firstplayer_cards)):
            print(firstplayer_cards[x])
            print(secondplayer_cards[x])
            winner = comparing_cards(firstplayer_cards[x], secondplayer_cards[x])
            if winner == 1:
                P1_score = P1_score + 1
                print("The first player won!")
            elif winner == 2:
                P2_score = P2_score + 1
                print("The second player won!")
            else:
                print("You Tied!")
        if P1_score > P2_score:
            print("The first player won, first player one has ", P1_score, " Points")
        elif P2_score > P1_score:
            print("The second player won, second player two has ", P2_score, " Points")
        else:
            print("First player score: ", P1_score)
            print("Second player score: ", P2_score)
    else:
        print("Sorry, have a nice day!")


def comparing_cards(firstcard, secondcard):
    """
    This function compares all of the cards dealt out and gives points to the player who won the games.
    :param firstcard: This function gives points to the first player if they win.
    :param secondcard: This function gives points to the second player if they win.
    :return: This function saves the points for each player.
    """
    if firstcard.rank > secondcard.rank:
        return 1
    elif firstcard.rank < secondcard.rank:
        return 2
    else:
        if firstcard.suit > secondcard.suit:
            return 1
        elif secondcard.suit > firstcard.suit:
            return 2


main()
