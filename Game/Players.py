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
        self.__ships_number = ships

    def setName(self, new_name):
        self.__name = new_name

    def setNumber(self, new_number):
        self.__number = new_number

    def setPositionalBoard(self, new_positional_board):
        self.__positional_board = new_positional_board

    def setMainBoard(self, new_main_board):
        self.__main_board = new_main_board

    def setShipsNumber(self, new_ships_number):
        self.__ships_number = new_ships_number

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

    def getPositionalBoard(self):
        return self.__positional_board

    def getMainBoard(self):
        return self.__main_board

    def getShipsNumber(self):
        return self.__ships_number

    def defineBoards(self):
        self.__positional_board.createBoard()
        self.__main_board.createBoard()

    '''def fire(self,):'''
