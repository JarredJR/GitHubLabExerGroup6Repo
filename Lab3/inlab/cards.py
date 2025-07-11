class Card(object):

    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    SUITS = ('Spades', 'Diamonds', 'Hearts', 'Clubs')

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit

import random

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self) == 0:
           return None
        else:
           return self.cards.pop(0)

    def __len__(self):
       return len(self.cards)

    def __str__(self): 
        result = ''
        for c in self.cards:
            result = self.result + str(c) + '\n'
        return result

def main():
    deck = Deck()
    print("A new deck:")
    while len(deck) > 0:
        print(deck.deal())
    deck = Deck()
    deck.shuffle()
    print("A deck shuffled once:")
    while len(deck) > 0:
        print(deck.deal())

if __name__ == "__main__":
    main()
    
