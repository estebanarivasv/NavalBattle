from Game import *
from Constants import *
from Ships import *
from Players import *
from Boards import *


cycle_menu = True
while cycle_menu:
    print("===============================================\n\n¡Bienvenido a Naval Battle Game!")
    print("Seleccioná una opción para continuar:")
    print(f"1.\tCrear partida",
          f"\n2.\tAyuda",
          f"\n3.\tSalir\n\n===============================================")

    op = editMenuOption()
    if op == 1:
        '''Instancia jugadores, tablero, juego. Aqui es donde va todo '''

        print("===============================================\nComenzaremos identificando a los jugadores\n")

        name1 = input("Ingrese el nombre del jugador 1: ")
        name2 = input("Ingrese el nombre del jugador 2: ")

        positional_board_player1 = Board("Tablero Posición", DEFAULT_BOARDS_ROWS_NUM, DEFAULT_BOARDS_COLUMNS_NUM)
        positional_board_player2 = Board("Tablero Posición", DEFAULT_BOARDS_ROWS_NUM, DEFAULT_BOARDS_COLUMNS_NUM)

        main_board_player1 = Board("Tablero Principal", DEFAULT_BOARDS_ROWS_NUM, DEFAULT_BOARDS_COLUMNS_NUM)
        main_board_player2 = Board("Tablero Principal", DEFAULT_BOARDS_ROWS_NUM, DEFAULT_BOARDS_COLUMNS_NUM)

        ships_player1 = []

        for i in range(DEFAULT_NUMBER_OF_AC):
            aircraft_carrier1 = Ship("Portaaviones", AIRCRAFT_CARRIER_ID, DEFAULT_AC_LENGTH)
            ships_player1.append(aircraft_carrier1)

        for i in range(DEFAULT_NUMBER_OF_SUB):
            submarine1 = Ship("Submarino", SUBMARINE_ID, DEFAULT_SUB_LENGTH)
            ships_player1.append(submarine1)

        for i in range(DEFAULT_NUMBER_OF_DES):
            destroyer1 = Ship("Destructor", DESTROYER_ID, DEFAULT_DES_LENGTH)
            ships_player1.append(destroyer1)

        for i in range(DEFAULT_NUMBER_OF_FRI):
            frigate1 = Ship("Fragata", FRIGATE_ID, DEFAULT_FRI_LENGTH)
            ships_player1.append(frigate1)

        ships_player2 = []

        for i in range(DEFAULT_NUMBER_OF_AC):
            aircraft_carrier2 = Ship("Portaaviones", AIRCRAFT_CARRIER_ID, DEFAULT_AC_LENGTH)
            ships_player2.append(aircraft_carrier2)

        for i in range(DEFAULT_NUMBER_OF_SUB):
            submarine2 = Ship("Submarino", SUBMARINE_ID, DEFAULT_SUB_LENGTH)
            ships_player2.append(submarine2)

        for i in range(DEFAULT_NUMBER_OF_DES):
            destroyer2 = Ship("Destructor", DESTROYER_ID, DEFAULT_DES_LENGTH)
            ships_player2.append(destroyer2)

        for i in range(DEFAULT_NUMBER_OF_FRI):
            frigate2 = Ship("Fragata", FRIGATE_ID, DEFAULT_FRI_LENGTH)
            ships_player2.append(frigate2)

        player1 = Player(name1, 1, positional_board_player1, main_board_player1, ships_player1)
        player2 = Player(name2, 2, positional_board_player2, main_board_player2, ships_player2)

        naval_battle = Game(player1, player2)

        naval_battle.shapeBoards()

        naval_battle.placeShips()

        naval_battle.startWar()

        break

    elif op == 2:
        print("\n\n===============================================\n\nEstás en AYUDA")
        print("Sólo puede haber dos jugadores: un jugador A y un jugador B.")
        print("Ambos dispondrán de dos tableros de 10 columnas por 10 filas:")
        print(f"\t-\tUn tablero POSICIÓN que le permitirá al jugador A posicionar sus barcos.")
        print(f"\t-\tUn tablero PRINCIPAL que les permitirá al jugador A disparar a los barcos del jugador B.")
        print("Los tipos de barcos que se pueden posicionar son cuatro:")
        print(f"\t-\tPortaaviones: ocupan 4 casilleros\t(cantidad disponible: 1)")
        print(f"\t-\t Submarinos: ocupan 3 casilleros\t(cantidad disponible: 1)")
        print(f"\t-\t Destructores: ocupan 2 casilleros\t(cantidad disponible: 1)")
        print(f"\t-\t Fragatas: ocupan 1 casillero\t\t(cantidad disponible: 2)")
        print("El juego se puede guardar y reanudarse en otro momento.\n===============================================")
        print(f"\nPresioná ENTER para volver atras.")
        input()

    elif op == 3:
        cycle_menu = False

    else:
        print("Has introducido un valor inválido.")
        op = editMenuOption()
