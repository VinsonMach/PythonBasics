# Vinson Mach 7/4/2022
# Second python game: A simple, automated card game of War, CPU vs CPU

import random

# Card suit dictionary
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# Card rank dictionary
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#Card value dictionary
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 
          'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# Card class that handles assigning ranks and suits
class Card:
    def __init__(self, suit, rank):
        self.suit = suit                                        # assign card suit
        self.rank = rank                                        # assign card rank
        self.value = values[rank]                               # assign card values

    def __str__(self):
        return self.rank + " of " + self.suit                   # return card information

# Deck class that handles card creation, shuffling, and card dealing
class Deck:
    def __init__(self):
        self.allCards = []                                      # initialize card list

        for suit in suits:
            for rank in ranks:
                createdCard = Card(suit, rank)                  # create card
                self.allCards.append(createdCard)               # add newly created card to card list

    def shuffle(self):
        random.shuffle(self.allCards)                           # shuffle card list

    def dealOne(self):
        return self.allCards.pop()                              # remove card from card list

# Player class handles adding and removing cards
class Player:
    def __init__(self, name):
        self.name = name                                        # assign name
        self.allCards = []                                      # initialize player card deck

    def removeOne(self):
        return self.allCards.pop(0)                             # remove player first card

    def addCards(self, newCards):
        if type(newCards) == type([]):
            self.allCards.extend(newCards)                      # extend card from player deck
        else:
            self.allCards.append(newCards)                      # add card to player deck

    def __str__(self):
        print('Player {} has {} cards.'.format(self.name, len(self.allCards)))  # print number of cards player has

# Main Function will handle game logic, intro and end
def main():
    p1 = Player("One")                                          # initialize player 1
    p2 = Player("Two")                                          # initialize player 2
    newDeck = Deck()                                            # initialize new deck
    newDeck.shuffle()                                           # shuffle new deck

    for x in range(26):
        p1.addCards(newDeck.dealOne())                          # deal half the deck to player 1
        p2.addCards(newDeck.dealOne())                          # deal the other half of the deck to player 2

    roundNum = 0                                                # initialize round counter
    gameOn = True                                               # continue game token
    atWar = True                                                # war calculation token

    while gameOn:
        roundNum += 1                                           # add 1 to round counter
        print("Round {}".format(roundNum))                      # print round number

        if len(p1.allCards) == 0:
            print('Player One is out of cards, Player Two wins.')   # print player 2 win statement
            gameOn = False                                          # end game
            break
        if len(p2.allCards) == 0:
            print('Player Two is out of cards, Player One wins.')   # print player 1 win statement
            gameOn = False                                          # end game
            break

        p1Cards = []                                            # initialize player 1 cards
        p1Cards.append(p1.removeOne())                          # add current player 1 card to player 1 deck
        p2Cards = []                                            # initialize player 2 cards
        p2Cards.append(p2.removeOne())                          # add current player 2 card to player 2 deck

        while atWar:
            if p1Cards[-1].value > p2Cards[-1].value:           # if last card in player 1 deck is greater than player 2 last card
                p1.addCards(p1Cards)                            # add current player 1 card to player 1 deck
                p1.addCards(p2Cards)                            # ass current player 2 card to player 1 deck
                atWar = False                                   # end war comparison 
            elif p1Cards[-1].value < p2Cards[-1].value:         # if last card in player 1 deck is lesser than player 2 last card
                p2.addCards(p1Cards)                            # add current player 1 card to player 2 deck
                p2.addCards(p2Cards)                            # add current player 2 card to player 2 deck
                atWar = False                                   # end war comparison
            else:
                print("War is taking place.")                   # print war occuring statement
                if len(p1.allCards) < 5:
                    print("Player 1 is unable to continue, Player 2 wins.") # print player 2 win statement
                    gameOn = False                                          # end game
                    break
                elif len(p2.allCards) < 5:
                    print("Player 2 is unable to continue, Player 1 wins.") # print player 1 win statement
                    gameOn = False                                          # end game
                    break
                else: 
                    for num in range(5):
                        p1Cards.append(p1.removeOne())          # add more cards to player 1
                        p2Cards.append(p2.removeOne())          # add more cards to player 2

if __name__ == "__main__":
    main()