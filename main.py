from random import shuffle
from random import randint

class Deck():

    #constructor
    def __init__(self):
        self.deck = []

    #assume numPlayer is either 3, 4, or 5
    #constraint checked in Game init
    def newDeck(self, numPlayer):
        self.deck =[]
        colorList = ['brown', 'yellow', 'green', 'orange', 'pink', 'gray', 'blue']
        if (numPlayer==3):
            Deck.makeNewDeck(self, colorList)
        else:
            del colorList[randint(0,len(colorList)-1)]
            Deck.makeNewDeck(self, colorList)
        shuffle(self.deck)
        self.deck.insert(15, 'last round')

    def makeNewDeck(self, colorList):
        for color in colorList:
            for num in range(9):
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


class Game():
    
    #constructor
    def __init__(self, numPlayers):
        if 2 < numPlayers < 6:
            self.numPlayers = numPlayers
        else:
            print("Must have between 3-5 players!")
    
    def game_init(self):
        #make and initialize Deck
        myDeck = Deck()
        myDeck.newDeck(self.numPlayers)
        print(myDeck.deck)

        #create Players, give each one a starting card
        playerList = []
        for num in range(self.numPlayers):
            playerList.append(Player())
            playerList[num].addCard(myDeck.deck.pop())
            print(playerList[num].hand)

def main():
    theGame = Game(3)
    theGame.game_init()
    theGame2 = Game(6)

main()
