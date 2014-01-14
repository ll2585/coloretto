from random import shuffle
from random import randint
from abc import ABCMeta, abstractmethod
import cmd
import string, sys
import settings as s

class Deck():

    #constructor
    def __init__(self, removeOneColor):
        self.deck = self.makeDeck(removeOneColor)

    def makeDeck(self, removeOneColor):
        def removeRandomColor():
            del colors[randint(0,len(colors)-1)]

        def addColorToDeck(color):
            deck.extend([color] * s.NUMBER_OF_CARDS_PER_COLOR)

        def addBonusCards():
            deck.extend([s.BONUS] * s.NUMBER_OF_BONUSES)

        def addJokers():
            deck.extend([s.JOKER] * s.NUMBER_OF_JOKERS)

        colors = s.COLORS
        deck = []
        if (removeOneColor):
            removeRandomColor()
        for color in colors:
            addColorToDeck(color)
        addBonusCards()
        addJokers()
        return deck

    def shuffleDeck(self):
        shuffle(self.deck)

    def addLastRoundIntoDeck(self):
        shuffle(self.deck)
        self.deck.insert(len(self.deck) - s.LAST_ROUND_CARD_POSITION, s.LAST_ROUND_CARD)

    def getDeck(self):
        return self.deck

    def removeCardAt(self, i):
        del self.deck[i]

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
        self.setUpGame()

    def setUpGame(self):
        self.makeDeck()
        self.setUpPlayers()
        self.setUpPiles()

    def startGame(self):
        def isColor(card):
            return card in s.COLORS

        def noOneHasColor(card):
            return card not in firstColors

        self.myDeck.shuffleDeck()
        firstColors = []
        for player in self.players:
            for i, card in enumerate(self.myDeck.getDeck()):
                if isColor(card) and noOneHasColor(card):
                    player.addCard(card)
                    firstColors.append(card)
                    self.myDeck.removeCardAt(i)
                    break
        self.myDeck.addLastRoundIntoDeck()
        self.gameStarted = True

    
    def game_init(self):
        
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
        self.myDeck = Deck(self.numPlayers==s.NUM_PLAYERS_TO_REMOVE_ONE_COLOR)

    def getDeck(self):
        return self.myDeck

    def setUpPlayers(self):
        self.players = [Player() for i in range(self.numPlayers)]

    def setUpPiles(self):
        self.pileList = [Pile() for i in range(self.numPlayers)]

    def getPlayers(self):
        return self.players
        


class GameImplementation(metaclass=ABCMeta):
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.initialize()

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def showDeck(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def showPlayers(self):
        pass

    @abstractmethod
    def showPile(self):
        pass

    def gameStarted(self):
        pass


class ConsoleGame(GameImplementation, cmd.Cmd):

    def __init__(self, numPlayers):
        cmd.Cmd.__init__(self)
        GameImplementation.__init__(self, numPlayers)
        self.prompt = '>>> '

    def initialize(self):
        pass

    def showDeck(self):
        pass

    def start(self):
        self.game = Game(self.numPlayers)
        self.game.startGame()


    def showPlayers(self):
        pass

    def showPile(self):
        pass

    def getDeck(self):
        return self.game.getDeck()

    def do_start(self, pileNumber):
        self.start()
        print(self.game.getDeck())

    def gameStarted(self):
        return self.game.gameStarted