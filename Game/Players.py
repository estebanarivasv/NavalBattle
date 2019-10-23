from Boards import *

class Player:
    def __init__(self, name="", number=0):
        self.__name = name
        self.__number = number
        self.position = Boards("Posición", 10, 10)
        self.principal = Boards("Principal", 10, 10)

    def setName(self, new_name):
        self.__name = new_name

    def setNumber(self, new_number):
        self.__number = new_number

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

def identifyPlayers():
    print("Identificación de jugadores\n")
    name1 = input("Ingrese el nombre del jugador 1: ")
    name2 = input("Ingrese el nombre del jugador 2: ")
    player1 = Player(name1, 1)
    player2 = Player(name2, 2)

    player1.principal.createBoard()
    player2.principal.createBoard()
    player1.position.createBoard()
    player2.position.createBoard()

