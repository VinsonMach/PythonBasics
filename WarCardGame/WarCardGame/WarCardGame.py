# Vinson Mach
# A simple card game of War, which is played against the CPU

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
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

# Deck class that handles
class Deck:
    def __init__(self):
        self.allCards = []

        for suit in suits:
            for rank in ranks:
                createdCard = Card(suit, rank)
                self.allCards.append(createdCard)