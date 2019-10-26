from Ships import *


class Boards:
    def __init__(self, name="", rows=0, columns=0):
        self.__name = name
        self.__rows = rows
        self.__columns = columns
        self.__board = []

    def setName(self, new_name):
        self.__name = new_name

    def setRows(self, new_rows):
        self.__rows = new_rows

    def setColumns(self, new_columns):
        self.__columns = new_columns

    def getName(self):
        return self.__name

    def setRows(self):
        return self.__rows

    def setColumns(self):
        return self.__columns

    def createBoard(self):
        for i in range(self.__rows):
            row = []
            for j in range(self.__columns):
                row.append(0)
            self.__board.append(row)

    def printBoard(self):
        k = 0
        print("      ", k, "  ", k + 1, "  ", k + 2, "  ", k + 3, "  ", k + 4, "  ", k + 5, "  ", k + 6, "  ", k + 7,
              "  ", k + 8, "  ", k + 9)
        print()
        for i in range(len(self.__board)):
            print(i, end="      ")
            for x in self.__board:
                print(x[i], end="    ")
            print()

    def insertShip(self, ship, row, column, orientation):
        """Orientation: horizontal (H) or vertical (V)"""
        # r = position_row
        # c = position_column
        # o = orientation
        if orientation == "H":
            if row + len(ship) > 9:
                print("No es posible posicionar el barco aquí. Por favor, definí una nueva posición.")
                self.insertShip(ship, editRowInfo(), editColumnInfo(), editOrientation())
            else:
                # booleano que se usa para verificar que esten vacios los cuadros en los que deberia entrar el barco
                place_chosen = False
                for i in range(len(ship)):
                    if self.__board[row + i][column] != 0:
                        place_chosen = True
                        print("Este casillero está ocupado. Por favor, definí una nueva posición.")
                        self.insertShip(ship, editRowInfo(), editColumnInfo(), editOrientation())
                if not place_chosen:
                    for i in range(len(ship)):
                        self.__board[row + i][column] = ship[i]

        elif orientation == "V":
            if column + len(ship) > 9:
                print("No es posible posicionar el barco aquí. Por favor, definí una nueva posicion")
                self.insertShip(ship, editRowInfo(), editColumnInfo(), editOrientation())
            else:
                place_chosen = False
                for i in range(len(ship)):
                    if self.__board[row][column + i] != 0:
                        place_chosen = True
                        print("Este casillero está ocupado. Por favor, definí una nueva posición.")
                        self.insertShip(ship, editRowInfo(), editColumnInfo(), editOrientation())
                if not place_chosen:
                    for i in range(len(ship)):
                        self.__board[row][column + i] = ship[i]


'''EXCEPTION HANDLING'''

def editRowInfo():
    while True:
        try:
            row = int(input("Fila: "))
            return row
        except ValueError:
            print("No ingresaste nada. Probá de nuevo.")


def editColumnInfo():
    try:
        column = int(input("Columna: "))
        return column
    except ValueError:
        print("No ingresaste nada. Probá de nuevo.")


def editOrientation():
    orientation = input("Orientación (H - horizontal, V - vertical): ")
    if len(orientation) == 0:
        print("No ingresaste nada. Probá de nuevo.")
        editOrientation()
    else:
        orientation = orientation.upper()
        return orientation
