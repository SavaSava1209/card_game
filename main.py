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
    
            
class Player:
    def __init__(self, name):
        self.name = name 
        self.cards = []

    def remove_one(self):
        return self.cards.pop()

    def add_cards(self, cards):
        if type(cards) == type([]):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

    def __str__(self):
        return f"{self.name} has {len(self.cards)} cards"


# game set up 
player1 = Player('one')
player2 = Player('two')
deck = Deck()
deck.shuffle()

for i in range(26):
    player1.add_cards(deck.deal_one())
    player2.add_cards(deck.deal_one())

game_on = True
round = 0
while game_on:
    round += 1
    print(f"{round} rounds")
    if len(player1.cards) == 0:
        print('Player2 wins')
        game_on = False
        break
    if len(player2.cards) == 0:
        print('Player1 wins')
        game_on = False
        break
    # start a new round
    player1_cards = []
    player1_cards.append(player1.remove_one())
    player2_cards = []
    player2_cards.append(player2.remove_one())


    at_war = True
    while at_war:
        
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            at_war = False

        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            at_war = False

        else:
           
            if len(player1.cards) < 5:
                print('player 1 unable to declare war, player2 wins')
                game_on = False
                break
            elif len(player2.cards) < 5:
                print('player 2 unable to declare war, player1 wins')
                game_on = False
                break
            else:
                for num in range(5):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())





