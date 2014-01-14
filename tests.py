
import game
import unittest
from unittest.mock import patch
from io import StringIO
import settings as s
import sys

class TestGameWorking(unittest.TestCase):

	def setUp(self):
		#nothing to set up yet
		#pass

		self.newGame = game.ConsoleGame(numPlayers=3)

	def tearDown(self):
		self.newGame = None

	def test_playerCountInRange(self):
		testGame = game.Game(numPlayers=3)
		testGame = game.Game(numPlayers=4)
		testGame = game.Game(numPlayers=5)

		with self.assertRaises(Exception):
			testGame = game.Game(numPlayers=1)
		with self.assertRaises(Exception):
			testGame = game.Game(numPlayers=2)
		with self.assertRaises(Exception):
			testGame = game.Game(numPlayers=6)


	def test_consoleGameIsImplementation(self):
		assert issubclass(game.ConsoleGame, game.GameImplementation)

	def test_consoleGameHasGame(self):
		self.newGame = game.ConsoleGame(numPlayers=3)
		self.newGame.start()
		self.game = self.newGame.game

	def test_consoleGameHasDeck(self):
		self.newGame = game.ConsoleGame(numPlayers=3)
		self.newGame.start()
		self.assertIsNotNone(self.newGame.getDeck())

	def test_everyoneHasColor(self):
		self.newGame = game.ConsoleGame(numPlayers=3)
		self.newGame.start()
		players = self.newGame.game.getPlayers()
		for p in players:
			self.assertIn(p.hand[0], s.COLORS)
			self.assertIs(len(p.hand),1)
		self.assertIsNot(players[0].hand[0], players[1].hand[0])
		self.assertIsNot(players[0].hand[0], players[2].hand[0])
		self.assertIsNot(players[1].hand[0], players[2].hand[0])

	def test_lastRoundInDeck(self):
		self.newGame = game.ConsoleGame(numPlayers=3)
		self.newGame.start()
		deck = self.newGame.game.getDeck().getDeck()
		cardsAfterLastRound = 0
		startCounting = False
		for i, card in enumerate(deck):
			if startCounting:
				cardsAfterLastRound+= 1
			elif card == s.LAST_ROUND_CARD:
				startCounting = True
		self.assertIs(cardsAfterLastRound,15)

	def test_gameStarts(self):
		self.newGame = game.ConsoleGame(numPlayers=3)
		self.newGame.start()
		deck = self.newGame.game.getDeck().getDeck()
		#self.newGame.cmdloop()
		self.newGame.onecmd("start")
		self.assertTrue(self.newGame.gameStarted())
		

if __name__ == '__main__':
	unittest.main(module=__name__)