from Players import *
from Boards import *
from Main import *


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






























def placeShips(player):
    print(f"\nDispondremos los barcos en el tablero principal del jugador N°{player.getNumber()}: {player.getName()}")
    a_c = 1
    sub = 1
    de = 1
    fr = 2
    while True:
        if a_c > 0:
            print(f"\n\nPosicioná tu portaaviones. Restantes {a_c}")
            player.principal.printBoard()
            print(
                "¿En qué posición querés poner tu portaaviones? Primero especificá el numero de fila y después el "
                "número de columna")
            player.principal.insertShip(aircraft_carrier, editRowInfo(), editColumnInfo(), editOrientation())
            a_c = a_c - 1
            printPrincipal(player)

        elif sub > 0:
            print(f"\n\nPosicioná tu submarino. Restantes {sub}")
            player.principal.printBoard()
            print(
                "¿En qué posición querés poner tu submarino? Primero especificá el numero de fila y después el "
                "número de columna")
            player.principal.insertShip(submarine, editRowInfo(), editColumnInfo(), editOrientation())
            sub = sub - 1
            printPrincipal(player)

        elif de > 0:
            print(f"\n\nPosicioná tu destructor. Restantes {de}")
            player.principal.printBoard()
            print(
                "¿En qué posición querés poner tu destructor? Primero especificá el numero de fila y después el "
                "número de columna")
            player.principal.insertShip(destroyer, editRowInfo(), editColumnInfo(), editOrientation())
            de = de - 1
            printPrincipal(player)

        elif fr > 0:
            print(f"\n\nPosicioná tu fragata. Restantes {fr}")
            player.principal.printBoard()
            print(
                "¿En qué posición querés poner tu fragata? Primero especificá el numero de fila y después el "
                "número de columna")
            player.principal.insertShip(frigate, editRowInfo(), editColumnInfo(), editOrientation())
            fr = fr - 1
            printPrincipal(player)

        elif a_c == 0 and sub == 0 and de == 0 and fr == 0:
            print("\n¡LISTO!")
            pass


def beginGame(player1, player2):
    while not player1.principal.nomoreShips():
        '''Verificar que hayan barcos por tirar.'''
        '''Pedirle al jugador que dispare.'''
        '''Modificar tablero posicion'''
        '''for i in range(len(player1.))'''
        '''Despues comparar'''
        print(
            f"\nPreparate jugador N°{player1.getNumber()}: {player1.getName()}. Tenés que adivinar dónde tiene los barcos el jugador N°{player2.getNumber()}")
        '''compareBoards(player2, player1)'''


'''def compareBoards(principal_board, positional_board):
    print
    pass

def fire
'''
