from Boards import *
from Ships import *
from Validations import *


class Player:
    __name = ""
    __number = 0
    __positional_board = []
    __main_board = []
    __ships = []

    def __init__(self, name, number, positional_board, main_board, ships):
        self.__name = name
        self.__number = number
        self.__positional_board = positional_board
        self.__main_board = main_board
        self.__ships = ships

    def setName(self, new_name):
        self.__name = new_name

    def setNumber(self, new_number):
        self.__number = new_number

    def setPositionalBoard(self, new_positional_board):
        self.__positional_board = new_positional_board

    def setMainBoard(self, new_main_board):
        self.__main_board = new_main_board

    def setShips(self, new_ships):
        self.__ships = new_ships

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def getPositionalBoard(self):
        return self.__positional_board

    def getMainBoard(self):
        return self.__main_board

    def getShips(self):
        return self.__ships

    def defineBoards(self):
        self.__positional_board.createPositionalBoard()
        self.__main_board.createMainBoard()

    def locateShipsInMainBoard(self):
        print(f"\n\nDefiniremos el tablero del jugador N°{self.getNumber()}: {self.getName()}")
        self.__main_board.shipsPosition(self.__ships)

    def attack(self, enemy):
        while True:
            self.__positional_board.displayBoard()
            print("\nIngresá la coordenada donde querés atacar.")
            coordinate = (editRowInfo(), editColumnInfo())
            row = coordinate[0]
            column = coordinate[1]
            if enemy.__main_board.isThereAShip(column, row):
                self.__positional_board[column][row] = enemy.__main_board[column][row]
                print("¡Tocado! Tenés otro turno")
                self.__positional_board.deleteSankPart(column, row)
                self.__positional_board.displayBoard()

            elif not enemy.__main_board.isThereAShip(column, row):
                self.__positional_board[column][row] = DEFAULT_WATER_ID_POSITION_BOARD
                print("¡Agua!")
                self.__positional_board.displayBoard()
                return False



