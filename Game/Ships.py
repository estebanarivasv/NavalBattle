from Constants import *
from Validations import *


class Ship:
    __name = ""
    __letter_id = 0
    __length = 0
    __initial_position = ()
    __final_coordinates = []

    def __init__(self, name, letter_id, length):
        self.__name = name
        self.__letter_id = letter_id
        self.__length = length

    def setName(self, new_name):
        self.__name = new_name

    def setId(self, new_id):
        self.__letter_id = new_id

    def setLength(self, new_length):
        self.__length = new_length

    def setInitialPosition(self):
        while True:
            print(f"\n¿En qué fila querés posicionar a tu {self.getName().lower()}?")
            row = editRowInfo()
            print(f"¿En qué columna querés posicionar a tu {self.getName().lower()}?")
            column = editColumnInfo()
            print(f"¿Qué orientación le querés dar al {self.getName().lower()}?")
            orientation = editOrientation()

            if ((column - 1) + self.__length) < DEFAULT_BOARDS_COLUMNS_NUM and row < DEFAULT_BOARDS_ROWS_NUM and orientation == "H":
                self.__initial_position = (row, column, orientation)
                return self.__initial_position
            elif ((row - 1) + self.__length) < DEFAULT_BOARDS_ROWS_NUM and column < DEFAULT_BOARDS_COLUMNS_NUM and orientation == "V":
                self.__initial_position = (row, column, orientation)
                return self.__initial_position
            else:
                print("Tu barco no se puede posicionar en las coordenadas que diste. Intentá de nuevo.")

    def setFinalCoordinates(self):
        row = self.__initial_position[0]
        column = self.__initial_position[1]
        orientation = self.__initial_position[2]
        ship_coordinates = []
        if orientation == "H":
            for i in range(self.__length):
                coordinates = (column + i, row)
                ship_coordinates.append(coordinates)
        elif orientation == "V":
            for i in range(self.__length):
                coordinates = (column, row + i)
                ship_coordinates.append(coordinates)
        return ship_coordinates

    def getName(self):
        return self.__name

    def getId(self):
        return self.__letter_id

    def getLength(self):
        return self.__length

    def getInitialPosition(self):
        return self.__initial_position

    def getFinalCoordinates(self):
        return self.__final_coordinates

