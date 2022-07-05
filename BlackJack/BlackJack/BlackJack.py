
# Vinson Mach 7/4/2022
# Third python game: A game of BlackJack

import random

# Card suit dictionary
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# Card rank dictionary
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#Card value dictionary
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 
          'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

playing = True

# Card class that handles assigning ranks and suits
class Card:
    def __init__(self, suit, rank):
        self.suit = suit                                        # assign card suit
        self.rank = rank                                        # assign card rank

    def __str__(self):
        return self.rank + " of " + self.suit                   # return card information

# Deck class that handles card creation, shuffling, and card dealing
class Deck:
    def __init__(self):
        self.deck = []                                          # initialize card list

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))              # add newly created card to card list

    def __str__(self):
        deckComp = ' '
        for card in self.deck:
            deckComp += '\n' + card.__str__()
        return "The deck has: " + deckComp

    def shuffle(self):
        random.shuffle(self.deck)                               # shuffle card list

    def dealOne(self):
        singleCard =  self.deck.pop()                           # remove card from card list
        return singleCard

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def addCard(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjustForAce(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, balance = 100):
        self.balance = 100
        self.bet = 0

    def winBet(self):
        self.balance += balance.bet

    def lostBet(self):
        self.balance -= balance.bet

def takeBet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Error: User input is not an integer")
        else:
            if chips.bet > chips.balance:
                print("Error: Invalid player chip balance, you have: {}".format(chips.balance))
            else:
                break

def hit(deck, hand):
    singleCard = deck.deal()
    hand.addCard(singleCard)
    hand.adjustForAce()

def hitOrStand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter H or S: ")
        if x[0].upper() == 'H':
            hit(deck, hand)
        elif x[0].upper() == 'S':
            print("Player stand, Dealer's Turn.")
            playing = False
        else:
            print("Error: Invalid input, please enter H or S")
            continue
        break

def showSome(player, dealer):
    print("\nDealer's Hand: ")
    print("First card is hidden.")
    print(dealer.cards[1])

    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

def showAll(player, dealer):
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)

    print("Value of Dealer's Hand: {}".format(dealer.value))
    
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
    print("Value of Player's Hand: {}".format(player.value))

def playerBusts(player, dealer, chips):
    print("Player Busts!")
    chips.loseBet()

def playerWin(player, dealer, chips):
    print("Player Wins!")
    chips.winBet()

def dealerBusts(player, dealer, chips):
    print("Dealer Busts!")
    chips.winBet()

def dealerWin(player, dealer, chips):
    print("Dealer Win!")
    chips.loseBet()

def push(player, dealer):
    print("Dealer and Player tie!")

# Main Function will handle game logic, intro and end
def main():

if __name__ == "__main__":
    main()