import random;
import pprint

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f" {self.rank} of {self.suit} "

class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(suit, rank))
        
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()   
    
            

card1 = Card('Dimonds', 'Two' )
deck1 = Deck()
deck1.shuffle()
my_card = deck1.deal_one()
print(my_card)
