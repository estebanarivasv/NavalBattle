from Validations import *
from Ships import *


def canFireBomb(column, row):
    if column < DEFAULT_BOARDS_COLUMNS_NUM and row < DEFAULT_BOARDS_ROWS_NUM:
        return True
    else:
        return False


class Board:
    __name = " "
    __rows = 0
    __columns = 0
    __board = []
    __placed_ships = []
    __deleted_ships_parts = []

    def __init__(self, name, rows, columns):
        self.__name = name
        self.__rows = rows
        self.__columns = columns

    def setName(self, new_name):
        self.__name = new_name

    def setRows(self, new_rows):
        self.__rows = new_rows

    def setColumns(self, new_columns):
        self.__columns = new_columns

    def setBoard(self, new_board):
        self.__board = new_board

    def setPlacedShips(self, new__placed_ships):
        self.__placed_ships = new__placed_ships

    def setDeletedShipsParts(self, new_deleted_ships_parts):
        self.__deleted_ships_parts = new_deleted_ships_parts

    def getName(self):
        return self.__name

    def getRows(self):
        return self.__rows

    def getColumns(self):
        return self.__columns

    def getBoard(self):
        return self.__board

    def getPlacedShips(self):
        return self.__placed_ships

    def getDeletedShipsParts(self):
        return self.__deleted_ships_parts

    def createMainBoard(self):
        self.__board = []
        for i in range(self.__rows):
            column = []
            for j in range(self.__columns):
                column.append(0)
                ''' Inserta un cero en cada espacio de la columna'''
            self.__board.append(column)

    def createPositionalBoard(self):
        self.__board = []
        for i in range(self.__rows):
            column = []
            for j in range(self.__columns):
                column.append("*")
                ''' Inserta un * en cada espacio de la columna'''
            self.__board.append(column)

    def displayBoard(self):
        print(f"\n{self.__name}:\n")
        k = 0
        print("      ", k, "  ", k + 1, "  ", k + 2, "  ", k + 3, "  ", k + 4, "  ", k + 5, "  ", k + 6, "  ", k + 7,
              "  ", k + 8, "  ", k + 9)
        print()
        for i in range(len(self.__board)):
            print(i, end="      ")
            for x in self.__board:
                print(x[i], end="    ")
            print()

    def areTheBoxesFree(self, ship_length, position):
        row = position[0]
        column = position[1]
        orientation = position[2]

        if orientation == "H":
            for j in range(ship_length):
                if self.__board[column + j][row] != 0:
                    return False
                if self.__board[column + j][row] == 0:
                    return True

        elif orientation == "V":
            for i in range(ship_length):
                if self.__board[column][row + i] != 0:
                    return False
                if self.__board[column][row + i] == 0:
                    return True

    def insertValue(self, column, row, value):
        self.__board[column][row] = value

    def isThereAShip(self, coordinate):
        for i in range(len(self.__placed_ships)):
            for j in self.__placed_ships[i]:
                if j == coordinate:
                    return True
                else:
                    return False

    def deleteSankPart(self, column, row):
        print("barcos ahi before ", self.__placed_ships)
        for i in range(len(self.__placed_ships)):
            for j in self.__placed_ships[i]:
                if j == (column, row):
                    print("elemento: ", j)
                    self.__placed_ships[i].remove(j)
                    self.__deleted_ships_parts.append(j)
                else:
                    pass
        print("barcos ahi after", self.__placed_ships)
