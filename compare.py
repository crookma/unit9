import card
import deck
newcard = card.Card(1, "Hearts")


def main():
    """

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

    :param firstplayer_cards:
    :param secondplayer_cards:
    :return:
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
        print("It was a tie")

def comparing_cards(firstcard, secondcard):
    """

    :param firstcard:
    :param secondcard:
    :return:
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
