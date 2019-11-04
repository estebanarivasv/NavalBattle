from Boards import *
from Ships import *


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
        print(f"\n\n=======================================================\n"
              f"Definiremos el tablero del jugador N°{self.getNumber()}: {self.getName()}")

        placed_ships = []
        for i in range(len(self.__ships)):
            self.getMainBoard().displayBoard()
            ship_length = self.__ships[i].getLength()

            while True:

                self.__ships[i].setInitialPosition()
                position = self.__ships[i].getInitialPosition()

                if self.getMainBoard().areTheBoxesFree(ship_length, position):
                    coordinates = self.__ships[i].setFinalCoordinates()
                    for k in coordinates:
                        column = k[0]
                        row = k[1]
                        self.getMainBoard().insertValue(column, row, self.__ships[i].getId())

                    placed_ships.append(coordinates)

                    break

                elif not self.getMainBoard().areTheBoxesFree(ship_length, position):
                    self.getMainBoard().displayBoard()
                    print("Este casillero está ocupado. Por favor, definí una nueva posición.")

            self.getMainBoard().displayBoard()
        print(placed_ships)
        self.getMainBoard().setPlacedShips(placed_ships)
        print(f"\n\n=======================================================\n\n")

    def attack(self, enemy):
        while True:
            print(f"\n\n=======================================================\n"
                  f"\nTurno de disparar del jugador N°{self.getNumber()}: {self.getName()}")
            self.__positional_board.displayBoard()
            print("\nIngresá la coordenada donde querés atacar.")
            while True:
                row = editRowInfo()
                column = editColumnInfo()
                coordinate = (column, row)

                if canFireBomb(row, column):
                    break
                elif not canFireBomb(row, column):
                    print("\nDefiní de nuevo tus coordenadas.")

            print("barcos del enemigo en su tabla\n", enemy.getMainBoard().getPlacedShips())

            if enemy.getMainBoard().isThereAShip(coordinate):
                print("¡Tocado! Tenés otro turno.")
                self.getPositionalBoard().getBoard()[column][row] = enemy.getMainBoard().getBoard()[column][row]
                enemy.getMainBoard().deleteSankPart(column, row)
                self.getPositionalBoard().displayBoard()

            elif not enemy.getMainBoard().isThereAShip(coordinate):
                print(coordinate)
                for i in enemy.getMainBoard().getDeletedShipsParts():
                    print(i)
                    if i == coordinate:
                        pass
                    else:
                        self.getPositionalBoard().getBoard()[column][row] = DEFAULT_WATER_ID_POSITION_BOARD
                        print("¡Agua!")
                self.getPositionalBoard().displayBoard()
                return False
