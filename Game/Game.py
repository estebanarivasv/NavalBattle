from Players import *
from Boards import *


class Game:

    def __init__(self, plyr1, plyr2):
        self.__player1 = plyr1
        self.__player2 = plyr2

    def setPlayer1(self, new_player1):
        self.__player1 = new_player1

    def setPlayer2(self, new_player2):
        self.__player2 = new_player2

    def getPlayer1(self):
        return self.__player1

    def getPlayer2(self):
        return self.__player2

    def shapeBoards(self):
        self.__player1.defineBoards()
        self.__player2.defineBoards()

    def placeShips(self):
        self.__player1.locateShipsInMainBoard()
        self.__player2.locateShipsInMainBoard()