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
        for i in range(self.__rows):
            column = []
            for j in range(self.__columns):
                column.append(0)
                ''' Inserta un cero en cada espacio de la columna'''
            self.__board.append(column)

    def displayBoard(self):
        k = 0
        print("      ", k, "  ", k + 1, "  ", k + 2, "  ", k + 3, "  ", k + 4, "  ", k + 5, "  ", k + 6, "  ", k + 7,
              "  ", k + 8, "  ", k + 9)
        print()
        for i in range(len(self.__board)):
            print(i, end="      ")
            for x in self.__board:
                print(x[i], end="    ")
            print()

    def shipsPositioning(self, ship, row, column, orientation):
        """Orientation: horizontal (H) or vertical (V)"""
        # r = position_row
        # c = position_column
        # o = orientation
        if orientation == "H":
            if row + len(ship) > 9:
                print("No es posible posicionar el barco acá. Por favor, definí una nueva posición.")
                self.insertShip(ship, editRowInfo(), editColumnInfo(), editOrientation())
            else:
                # booleano que se usa para verificar que esten vacios los cuadros en los que deberia entrar el barco
                place_chosen = False
                for i in range(len(ship)):
                    if self.__board[column + i][row] != 0:
                        place_chosen = True
                        print("Este casillero está ocupado. Por favor, definí una nueva posición.")
                        self.insertShip(ship, editRowInfo(), editColumnInfo(), editOrientation())
                if not place_chosen:
                    for i in range(len(ship)):
                        self.__board[column + i][row] = ship[i]

        elif orientation == "V":
            if column + len(ship) > 9:
                print("No es posible posicionar el barco aquí. Por favor, definí una nueva posicion")
                self.insertShip(ship, editRowInfo(), editColumnInfo(), editOrientation())
            else:
                place_chosen = False
                for i in range(len(ship)):
                    if self.__board[column][row + i] != 0:
                        place_chosen = True
                        print("Este casillero está ocupado. Por favor, definí una nueva posición.")
                        self.insertShip(ship, editRowInfo(), editColumnInfo(), editOrientation())
                if not place_chosen:
                    for i in range(len(ship)):
                        self.__board[column][row + i] = ship[i]

    def noMoreShips(self):
        ships_sank = self.__board.count("T")
        if ships_sank == 11:
            return True
        elif 0 < ships_sank < 11:
            return False


