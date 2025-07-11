from cards import Deck
class Player(object):
    
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        result = ", ".join(map(str, self.cards))
        result += "\n  " + str(self.getPoints()) + " points"
        return result

    def hit(self, card):
        self.cards.append(card)

    def getPoints(self):
        count = 0
        for card in self.cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        for card in self.cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def hasBlackjack(self):
        return len(self.cards) == 2 and self.getPoints() == 21 


class Dealer(Player):

    def __init__(self, cards):
        Player.__init__(self, cards)
        self.showOneCard = True

    def __str__(self):
        if self.showOneCard:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):

        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())

class Blackjack(object):

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

    def play(self):
        print("Player:\n", self.player)
        print("Dealer:\n", self.dealer)
        while True:
            choice = input("Do you want a hit? [y/n]: ")
            if choice in ("Y", "y"):
                self.player.hit(self.deck.deal())
                points = self.player.getPoints()
                print("Player:\n", self.player)
                if points >= 21:
                    break
            else:
                break
        playerPoints = self.player.getPoints()
        if playerPoints > 21:
            print("You bust and lose")
        else:
            self.dealer.hit(self.deck)
            print("Dealer:\n", self.dealer)
            dealerPoints = self.dealer.getPoints()
            if dealerPoints > 21:
                print("Dealer busts and you win")
            elif dealerPoints > playerPoints:
                print("Dealer wins")
            elif dealerPoints < playerPoints and playerPoints <= 21:
                print("You win")
            elif dealerPoints == playerPoints:
                if self.player.hasBlackjack() and not self.dealer.hasBlackjack():
                    print("You win")
                elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():
                    print("Dealer wins")
                else:
                    print("There is a tie")
        
def main():
    game = Blackjack()
    game.play()

if __name__ == "__main__":
    main()
  
