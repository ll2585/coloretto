from random import shuffle
from random import randint
import cmd
import string, sys
import settings as s

class Deck():

    #constructor
    def __init__(self):
        self.deck = []
        self.startingColorList = []

    #assume numPlayer is either 3, 4, or 5
    #constraint checked in Game init
    def newDeck(self, numPlayer):
        self.deck =[]
        colorList = ['brown', 'yellow', 'green', 'orange', 'pink', 'gray', 'blue']
        self.startingColorList = []
        #edit this later if/when asking players for initial color
        for i in range(numPlayer):
            randomInt = randint(0, len(colorList)-1)
            self.startingColorList.append(colorList[randomInt])
            del colorList[randomInt]         
        if (numPlayer!=3):
            Deck.makeNewDeck(self, colorList, self.startingColorList)
        else:
            del colorList[randint(0,len(colorList)-1)]
            Deck.makeNewDeck(self, colorList, self.startingColorList)
        shuffle(self.deck)
        self.deck.insert(15, 'last round')

    def makeNewDeck(self, colorList, startingColorList):
        for color in colorList:
            for num in range(9):
                self.deck.append(color)
        for color in startingColorList:
            for num in range(8):
                self.deck.append(color)
        for num in range(10):
            self.deck.append('+2')
        for num in range(3):
            self.deck.append('joker')    

class Player():

    #constructor
    def __init__(self):
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

class Card():
    def __init__(self, card):
        self.card = card

    def setCard(self, card):
        self.card = card

    def getCard(self):
        return self.card


class CLI(cmd.Cmd):
    
    def __init__(self, myDeck, playerList, pileList, currentCard):
        cmd.Cmd.__init__(self)
        self.myDeck = myDeck
        self.playerList = playerList
        self.pileList = pileList
        self.currentCard = currentCard
        self.prompt = '>>> '

    #def cmdloop(self, currentCard):
        
        #return cmd.Cmd.cmdloop(self, currentCard)

    def do_DRAW(self, arg):
        card = self.myDeck.deck.pop()
        print("you drew " + card)
        self.currentCard.setCard(card)
        print("on which pile will you PLACE it?")
        CLI.printPiles(self, self.pileList)

    def printPiles(self, pileList):
        for p in self.pileList:
            print((p.pile))

   # def getCard(self):
       # return self.currentCard

    def moveCard(self, card, pileNumber):
        self.pileList[int(pileNumber)].pile.append(card.getCard())

    def do_TAKE(self, pileNumber):
        print("you took pile" + pileNumber)

    def do_PLACE(self, pileNumber):
        CLI.moveCard(self, self.currentCard, pileNumber)
        print("you placed " + self.currentCard.getCard() + " on pile " +pileNumber)
        CLI.printPiles(self, self.pileList)
        

class Pile():
    #constructor
    def __init__(self):
        self.pile = []
    
    def addToPile(self, card):
        self.pile.append(card)

    def clearPile(self):
        self.pile[:] = []

class Game():
    #constructor
    def __init__(self, numPlayers):
        if s.MIN_PLAYERS < numPlayers < s.MAX_PLAYERS:
            self.numPlayers = numPlayers
        else:
            print("Must have between 3-5 players!")
            raise Exception
    
    def game_init(self):
        self.makeDeck()
        print(self.myDeck.deck)

        #create Players, give each one a starting card
        playerList = []
        pileList = []
        for num in range(self.numPlayers):
            playerList.append(Player())
            playerList[num].addCard(self.myDeck.startingColorList.pop())
            pileList.append(Pile())
            print((playerList[num].hand))
            print((pileList[num].pile))
        currentCard = Card('')
        cli = CLI(self.myDeck, playerList, pileList, currentCard)
        #currentCard = 'brown'
        cli.cmdloop()

    def makeDeck(self):
        self.myDeck = Deck()
        self.myDeck.newDeck(self.numPlayers)
        

def main():
    theGame = Game(numPlayers=3)
    theGame.game_init()
    #theGame2 = Game(6)

if __name__ == '__main__':
    main()
