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

    def startWar(self):
        while True:
            if self.__player1.getTerminateGame() is False and self.__player2.getTerminateGame() is False:
                while True:
                    self.__player1.attack(self.__player2)
                    if self.__player2.getTerminateGame() is True:
                        break
                    self.__player2.attack(self.__player1)
                    if self.__player1.getTerminateGame() is True:
                        break

            elif self.__player1.getTerminateGame() is True and self.__player2.getTerminateGame() is False:
                print("\n\n¡Juego terminado!")
                print(f"JUGADOR GANADOR N°{self.__player2.getNumber()}: {self.__player2.getName()}")
                break

            elif self.__player1.getTerminateGame() is False and self.__player2.getTerminateGame() is True:
                print("\n\n¡Juego terminado!")
                print(f"JUGADOR GANADOR N°{self.__player1.getNumber()}: {self.__player1.getName()}")
                break
