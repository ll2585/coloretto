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

class Game():
    
    #constructor
    def __init__(self, numPlayers):
        if 2 < numPlayers < 6:
            self.numPlayers = numPlayers
        else:
            print("Must have between 3-5 players!")
    
    @classmethod
    def get_numPlayers(cls):
        return cls.numPlayers
    
    myDeck = Deck()
    myDeck.newDeck(get_numPlayers)
    print(myDeck.deck)

    

def main():
    theGame = Game(3)
    theGame2 = Game(6)

main()
