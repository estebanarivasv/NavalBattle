from Constants import *
from Validations import *


class Ship:
    __name = ""
    __letter_id = 0
    __length = 0
    __position = ()

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

    def setPosition(self):
        while True:
            print("¿En qué fila querés posicionar tu barco?")
            row = editRowInfo()
            print("¿En qué columna querés posicionar tu barco?")
            column = editColumnInfo()
            print("¿Qué orientación le querés dar al barco?")
            orientation = editOrientation()

            if (row + self.__length) < DEFAULT_BOARDS_ROWS_NUM and orientation == "H":
                self.__position = (row, column, orientation)
                return self.__position
            elif (column + self.__length) < DEFAULT_BOARDS_COLUMNS_NUM and orientation == "V":
                self.__position = (row, column, orientation)
                return self.__position
            else:
                print("Tu barco no se puede posicionar en las coordenadas que diste. Intentá de nuevo.")

    def getName(self):
        return self.__name

    def getId(self):
        return self.__letter_id

    def getLength(self):
        return self.__length

    def getPosition(self):
        return self.__position


def createShips():
    ships = []

    for i in range(DEFAULT_NUMBER_OF_AC):
        aircraft_carrier = Ship("Portaaviones", AIRCRAFT_CARRIER_ID, DEFAULT_AC_LENGTH)
        ships.append(aircraft_carrier)

    for i in range(DEFAULT_NUMBER_OF_SUB):
        submarine = Ship("Submarino", SUBMARINE_ID, DEFAULT_SUB_LENGTH)
        ships.append(submarine)

    for i in range(DEFAULT_NUMBER_OF_DES):
        destroyer = Ship("Destructor", DESTROYER_ID, DEFAULT_DES_LENGTH)
        ships.append(destroyer)

    for i in range(DEFAULT_NUMBER_OF_FRI):
        frigate = Ship("Fragata", FRIGATE_ID, DEFAULT_FRI_LENGTH)
        ships.append(frigate)

    return ships
