
# Vinson Mach 7/4/2022
# Third python game: A game of BlackJack with betting

import random

# Card suit dictionary
suits = ('♥', '♦', '♣', '♠')

# Card rank dictionary
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

# Card value dictionary
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
          '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

playing = True

# Card class that handles assigning ranks and suits
class Card:
    def __init__(self, suit, rank):
        self.suit = suit                                        # assign card suit
        self.rank = rank                                        # assign card rank

    def __str__(self):
        return self.rank + self.suit                            # return card information

# Deck class that handles card creation, shuffling, and card dealing
class Deck:
    def __init__(self):
        self.deck = []                                          # initialize card list

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))              # add newly created card to card list

    def __str__(self):
        deckComp = ' '                                          # number of cards in deck
        for card in self.deck:
            deckComp += '\n' + card.__str__()                   # add card to deck
        return "The deck has: " + deckComp                      # return deck statement

    def shuffle(self):
        random.shuffle(self.deck)                               # shuffle card list

    def dealCard(self):
        singleCard =  self.deck.pop()                           # remove card from card list
        return singleCard                                       # return single card

# Hand class handles cards in hand
class Hand:
    def __init__(self):
        self.cards = []                                         # initializes card list
        self.value = 0                                          # inititalize card value
        self.aces = 0                                           # inititalize ace count

    def addCard(self, card):
        self.cards.append(card)                                 # add card to card list
        self.value += values[card.rank]                         # get card value

        if card.rank == 'Ace':
            self.aces += 1                                      # increment ace count

    def adjustForAce(self):
        while self.value > 21 and self.aces:
            self.value -= 10                                    # make ace value = 1
            self.aces -= 1                                      # decrement ace value

# Chip class handles player betting chips
class Chips:
    def __init__(self, balance = 100):
        self.balance = 100                                      # initialize default player chip balance = 100
        self.bet = 0                                            # initialize player bet

    def winBet(self):
        self.balance += self.bet                                # add player bet to player balance

    def lostBet(self):
        self.balance -= self.bet                                # subtract player bet to player balance

# takeBet function handles player bet
def takeBet(chips):
    while True:
        try:
            print("Current Chip Balance: {} ".format(chips.balance))                                # print current player ship balance
            chips.bet = int(input("How many chips would you like to bet? "))                        # ask user for bet amount
        except:
            print("Error: User input is not an integer")                                            # print error statement
        else:
            if chips.bet > chips.balance:
                print("Error: Invalid player chip balance, you have: {}".format(chips.balance))     # print error statement
            else:
                break

# hit function handles adding card to hand
def hit(deck, hand):
    singleCard = deck.dealCard()                                # pull a single card from deck
    hand.addCard(singleCard)                                    # add single card to hand
    hand.adjustForAce()                                         # check for ace and readjust

# hitOrStand function handles player hitting or standing
def hitOrStand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter H or S: ")               # ask user for input
        if x[0].upper() == 'H':
            hit(deck, hand)                                     # player hit if input is 'h'
        elif x[0].upper() == 'S':
            print("\nPlayer stand, Dealer's Turn.")             # print turn switch statement
            playing = False                                     # switch turns
        else:
            print("Error: Invalid input, please enter H or S")  # print error statement
            continue
        break

# showSome function handles showing dealer's second card and all player cards
def showSome(player, dealer):
    print("\n-----------------------------------")                      # print beginning of turn spacer
    print("Dealer's Hand: ")                                            # print dealers hand statement
    print("First card is hidden.")                                      # print hidden card statement
    print(dealer.cards[1])                                              # print second card
    print("Value of Dealer's Hand: {}".format(dealer.cards[1].rank))    # print value of dealer's second card

    print("\nPlayer's Hand: ")                                          # print players hand statement
    for card in player.cards:
        print(card)                                                     # print all player's cards
    print("Value of Player's Hand: {}".format(player.value))            # print value of all player's cards
    print("-----------------------------------\n")                      # print end of turn spacer

# showAll function handles showing all cards dealt
def showAll(player, dealer):
    print("\n-----------------------------------")                      # print beginning of turn spacer
    print("Dealer's Hand: ")                                            # print dealer's hand statement
    for card in dealer.cards:
        print(card)                                                     # print all dealer's cards
    print("Value of Dealer's Hand: {}".format(dealer.value))            # print value of all dealer's cards
    
    print("\nPlayer's Hand: ")                                          # print player hand statement
    for card in player.cards:
        print(card)                                                     # print all player's cards
    print("Value of Player's Hand: {}".format(player.value))            # print value of all player cards
    print("-----------------------------------\n")                      # print end of turn spacer

# playerBusts function handles player busting
def playerBusts(player, dealer, chips):
    print("Player Busts!")                                      # print player bust statement
    chips.lostBet()                                             # subtract player bet from player balance

# playerWin function handles player winning
def playerWin(player, dealer, chips):
    print("Player Wins!")                                       # print player win statement
    chips.winBet()                                              # add player bet to player balance

# dealerBusts function handles dealer busting
def dealerBusts(player, dealer, chips): 
    print("Dealer Busts!")                                      # print dealer bust statement
    chips.winBet()                                              # add player bet to player balance

# dealerWin function handles dealer winning
def dealerWin(player, dealer, chips):
    print("Dealer Win!")                                        # print dealer win statement
    chips.lostBet()                                             # subtract player bet from player balace

# push function handles tie between player and dealer
def push(player, dealer):
    print("Dealer and Player tie!")                             # print tie statement

# Main Function will handle game logic, intro and end
def main():
    while True:
        print("\nWelcome to BlackJack\n")                       # print welcome statement
        deck = Deck()                                           # initialize new deck
        deck.shuffle()                                          # shuffle new deck
        global playing

        playerHand = Hand()                                     # initialize player hand
        playerHand.addCard(deck.dealCard())                     # add first card to player hand
        playerHand.addCard(deck.dealCard())                     # add second card to player hand

        dealerHand = Hand()                                     # initialize dealer hand
        dealerHand.addCard(deck.dealCard())                     # add first card to dealer hand
        dealerHand.addCard(deck.dealCard())                     # add second card to dealer hand

        playerChips = Chips()                                   # initalize player chips
        takeBet(playerChips)                                    # take bet from player
        showSome(playerHand, dealerHand)                        # show dealer's second card and all player cards

        while playing:  
            hitOrStand(deck, playerHand)                        # ask player if they want to hit for stand
            showSome(playerHand, dealerHand)                    # show dealer's second card and all player cards

            if playerHand.value > 21:
                playerBusts(playerHand, dealerHand, playerChips)    # player bust
                break

        if playerHand.value <= 21:
            while dealerHand.value < playerHand.value:
                hit(deck, dealerHand)                               # dealer hit

            showAll(playerHand, dealerHand)                         # show all cards

            if dealerHand.value > 21:
                dealerBusts(playerHand, dealerHand, playerChips)    # dealer busts
            elif dealerHand.value > playerHand.value:
                dealerWin(playerHand, dealerHand, playerChips)      # dealer wins
            elif dealerHand.value < playerHand.value:
                playerWin(playerHand, dealerHand, playerChips)      # player wins
            else:
                push(playerHand, dealerHand, playerChips)           # push

        print('\nPlayer Chip Balance: {}'.format(playerChips.balance))  # print player chip balance
        newGame = input("\nWould you like to play again (Y/N)? ")       # ask user if they would like to play again

        if newGame[0].upper() == 'Y':   
            playing = True                                          # play another round
            continue
        else:
            print("Thank you for playing!")                         # print thank you statement
            break

if __name__ == "__main__":
    main()