'''
Created on Oct 12, 2018

@author: apoorva
'''
import random

suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank +' of '+self.suit
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deckcontent = ''
        for card in self.deck:
            deckcontent = card.__str__() + '\n'
        return deckcontent
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        top_card = self.deck.pop(0)
        return top_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 #attribute to keep track of the aces
        
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        
    def decide_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total):
        self.total = total
        self.bet = 0
        
    def win(self):
        self.total += self.bet
        
    def lose(self):
        self.total -= self.bet
    
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Choose your bet amount: '))
        except ValueError:
            print("Please enter integer...")
        else:
            if chips.bet > chips.total:
                print("Can't bet more than what you have....", chips.total)
                continue
            else:
                break
    return chips.bet

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.decide_for_aces()
    
def hit_or_stand(deck, hand):
    global playing
    while True:
        decision = input("Would you like to Hit or Stand? Enter 'h' or 's'").lower()
        
        if decision not in ['h', 's']:
            print("Wrong input. ")
            continue
        elif decision == 'h':
            hit(deck, hand)
            break
        elif decision == 's':
            print("Player stands. Dealer playing. ")
            playing = False
            break
        else:
            pass

def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden> ", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep = "\n ")
    
def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep = "\n ")
    print(" Dealer Total: ", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep = "\n ")           
    print(" Your total: ", player.value) 
    
def player_busts(player, dealer, chips):
    print("Player busts! ")
    chips.lose()
    
def player_wins(player, dealer, chips):
    print("Player wins! ")
    chips.win()
    
def dealer_busts(player, dealer, chips):
    print("Dealer busts! ")
    chips.win()
    
def dealer_wins(player, dealer, chips):
    print("Dealer wins! ")
    chips.lose()
    
def push(player, dealer):
    print("Tie! It's a push. ")

    
print("Welcome to BlackJack! ")
print("Get as close to 21 as you can without going over! \n Dealer hits until she reaches 17. Aces count as 1 or 11.")

chips_total = 500
while True:
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    
    #Deal two cards 
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    #set up chips
    player_chips = Chips(chips_total)
    
    bet = take_bet(player_chips)
    
    print("Player has ",player_chips.total, " and  bets ", bet, " chips.")
    
    status = ' '
    
    #show all the top cards, but one dealer card
    show_some(player_hand, dealer_hand)
    
    while playing:
        #prompt for hit or stand
        hit_or_stand(deck, player_hand)
        
        show_some(player_hand, dealer_hand)
    
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            status = 'lost'
            break
        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
            
        show_all(player_hand, dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
            status = 'won'
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
            status = 'lost'
            
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            status = 'won'
            
        else:
            push(player_hand, dealer_hand)
    
    print("\nPlayer's winnings stand at ", player_chips.total)
    chips_total = player_chips.total
    
    play_again = input("Would you like to play another hand? ").lower()
    if play_again == 'yes' or 'y':
        continue
    else:
        print("Thanks for playing! ")
        break
        
        

        

