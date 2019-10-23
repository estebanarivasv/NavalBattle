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
        k=0
        print("      ", k, "  ", k+1, "  ", k+2, "  ", k+3, "  ", k+4, "  ", k+5, "  ", k+6, "  ", k+7, "  ", k+8, "  ", k+9)
        print()
        for i in range(len(self.__board)):
            print(i, end="      ")
            for x in self.__board:
                print(x[i], end="    ")
            print()
