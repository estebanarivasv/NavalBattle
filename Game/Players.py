from Boards import *
from Ships import *


class Player:
    __name = ""
    __number = 0
    __positional_board = []
    __main_board = []
    __ships = []
    __terminate_game = False

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

    def setTerminateGame(self, new_terminate_game):
        self.__terminate_game = new_terminate_game

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

    def getTerminateGame(self):
        return self.__terminate_game

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
        self.getMainBoard().setPlacedShips(placed_ships)
        print(f"\n\n=======================================================\n\n")

    def isPlacedShipsEmpty(self):
        c = 0
        for i in self.getMainBoard().getPlacedShips():
            if len(i) == 0:
                c = c + 1
                if c == DEFAULT_NUMBER_OF_SHIPS:
                    return True
            else:
                pass
        return False

    def attack(self, enemy):
        is_enemy_placed_ships_list_empty = enemy.isPlacedShipsEmpty()
        while not is_enemy_placed_ships_list_empty:
            if enemy.isPlacedShipsEmpty():
                break
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

                if enemy.getMainBoard().isThereAShipPart(coordinate):

                    if enemy.getMainBoard().isInDeletedShipsParts(coordinate):
                        self.getPositionalBoard().displayBoard()
                        print("Esta parte ya la habías hundido. Perdés el turno.")
                        return False

                    elif not enemy.getMainBoard().isInDeletedShipsParts(coordinate):
                        print("¡Tocado! Tenés otro turno.")
                        self.getPositionalBoard().getBoard()[column][row] = DEFAULT_SANK_PART_ID_POSITION_BOARD
                        enemy.getMainBoard().deleteSankPart(column, row)
                        self.getPositionalBoard().displayBoard()

                        if enemy.isPlacedShipsEmpty():
                            break

                elif not enemy.getMainBoard().isThereAShipPart(coordinate):

                    if not enemy.getMainBoard().isInDeletedShipsParts(coordinate):
                        self.getPositionalBoard().getBoard()[column][row] = DEFAULT_WATER_ID_POSITION_BOARD
                        print("¡Agua!")
                        self.getPositionalBoard().displayBoard()
                        return False

        enemy.setTerminateGame(True)
