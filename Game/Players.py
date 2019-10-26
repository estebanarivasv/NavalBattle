from Boards import *
from Ships import *

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

    placeShips(player1)
    placeShips(player2)

def printPrincipal(player):
    print("Tablero resultante: ")
    player.principal.printBoard()
    input("Presioná enter para seguir.")




def placeShips(player):
    print(f"Dispondremos los barcos en el tablero principal del jugador N°{player.getNumber()}: {player.getName()}")
    a_c = 1
    sub = 1
    de = 1
    fr = 2
    while True:
        if a_c > 0:
            print(f"Posicioná tu portaaviones. Restantes {a_c}")
            player.principal.printBoard()
            print("¿En qué posición querés poner tu portaaviones? Primero especificá el numero de fila y después el numero de columna")
            row = int(input("Fila: "))
            column = int(input("Columna: "))
            orientation = input("Orientación (H - horizontal, V - vertical): ")
            orientation = orientation.upper()
            player.principal.insertShip(a_carrier, row, column, orientation)
            a_c = a_c - 1
            printPrincipal(player)

        elif sub > 0:
            print(f"Posicioná tu submarino. Restantes {sub}")
        elif de > 0:
            print(f"Posicioná tu destructor. Restantes {de}")
        elif fr > 0:
            print(f"Posicioná tu fragata. Restantes {fr}")
        elif a_c == 0 and sub == 0 and de == 0 and fr == 0:
            pass

