import random
import pprint

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':1}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]



    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(suit, rank))
      

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += '\n' + card.__str__()
        return f"This deck has {deck_comp} "

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# used to calculate the values and adjust ace  value
class Hand:
    def __init__(self):
        self.cards = []
        self.values = 0
        # track aces
        self.aces = 0        

    def add_card(self, card):
        self.cards.append(card)
        self.values += card.value

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        while self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1

class Chip:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
    

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print('Sorry, a bet must be an integer')
        else:
            if chips.bet > chips.total:
                print(f"Sorry your bet can't exceed. You have {chips.total}.")
            else:
                break

def hit(deck, hand):
    one_card = deck.deal_card()
    hand.add_card(one_card)
    hand.adjust_ace()

playing = True
def hit_or_stand(deck, hand):
    global playing
    while playing:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Dealer's turn")
            playing = False

        else:
            print('Sorry I dont understand')
        break

def show_some(player, dealer):
    # show only one of the dealer's cards
    print("Dealer's hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # show all of the player's hand/cards
    print("\nPlayer's hand: ")    
    for card in player.cards:       
        print(card)

def show_all(player, dealer):
    print(" Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Values of dealer's card is : {dealer.values} \n")

    print(" Player's hand: ")
    for card in player.cards:
        print(card)
    print(f"Values of player's card is : {player.values}\n")

def player_busts(player, dealer, chips):
    print("Bust player")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Player wins, Bust dealer")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("dealer wins")
    chips.lose_bet() 

def push(player, dealer):
    print("Dealer and player tie! PUSH")


while True:
    print("Welcom to Black Jack")

    deck = Deck()
    deck.shuffle()

    player = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())

    dealer = Hand()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

    # set up player's chip 
    player_chips = Chip()

    take_bet(player_chips)

    show_some(player, dealer)

    while playing:
        hit_or_stand(deck, player)
        show_some(player, dealer)

        if player.values > 21:
            player_busts(player, dealer, player_chips)
            break

    if player.values <= 21:
        while dealer.values < 17:
            hit(deck, dealer)

        show_all(player, dealer)
        if dealer.values > 21:
            dealer_busts(player, dealer, player_chips)
        elif dealer.values > player.values:
            dealer_wins(player, dealer, player_chips)
        elif dealer.values < player.values:
            player_wins(player, dealer, player_chips)
        else:
            push(player, dealer)
    print(f'player total chips are at {player_chips.total}')

    new_game = input('Would you like to play another hand? y/n ')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing!')
        break


