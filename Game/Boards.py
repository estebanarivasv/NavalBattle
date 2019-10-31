from Validations import *
from Ships import *


class Board:
    __name = " "
    __rows = 0
    __columns = 0
    __board = []

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

    def getName(self):
        return self.__name

    def getRows(self):
        return self.__rows

    def getColumns(self):
        return self.__columns

    def getBoard(self):
        return self.__board

    def createBoard(self):
        self.__board = []
        for i in range(self.__rows):
            column = []
            for j in range(self.__columns):
                column.append(0)
                ''' Inserta un cero en cada espacio de la columna'''
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

    def shipsPosition(self, ships):
        total_ships_coordinates = []
        for i in range(len(ships)):
            self.displayBoard()
            ships[i].setInitialPosition()
            position = ships[i].getInitialPosition()
            ship_length = ships[i].getLength()

            while True:
                if self.areTheBoxesFree(ship_length, position):
                    coordinates = ships[i].setFinalCoordinates()
                    for k in coordinates:
                        column = k[0]
                        row = k[1]
                        self.insertValue(column, row, ships[i].getId())
                    break

                elif not self.areTheBoxesFree(ship_length, position):
                    self.displayBoard()
                    print("Este casillero está ocupado. Por favor, definí una nueva posición.")
                    ships[i].setInitialPosition()

        return total_ships_coordinates
