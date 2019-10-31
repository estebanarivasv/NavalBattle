from Game import *
from Constants import *
from Ships import *
from Players import *
from Boards import *

print("¡Bienvenido a Naval Battle Game!")
print("Seleccioná una opción para continuar:")
print(f"1.\tCrear partida",
      f"\n2.\tCargar partida guardada",
      f"\n3.\tAyuda",
      f"\n4.\tSalir")

op = editMenuOption()

cycle_menu = True
while cycle_menu:
    if op == 1:
        '''Instancia jugadores, tablero, juego. Aqui es donde va todo '''

        print("\nComenzaremos identificando a los jugadores\n")

        name1 = input("Ingrese el nombre del jugador 1: ")
        name2 = input("Ingrese el nombre del jugador 2: ")

        positional_board = Board("Tablero Posición", DEFAULT_BOARDS_ROWS_NUM, DEFAULT_BOARDS_COLUMNS_NUM)
        main_board = Board("Tablero Principal", DEFAULT_BOARDS_ROWS_NUM, DEFAULT_BOARDS_COLUMNS_NUM)

        player1 = Player(name1, 1, positional_board, main_board, createShips())
        player2 = Player(name2, 2, positional_board, main_board, createShips())

        naval_battle = Game(player1, player2)

        naval_battle.shapeBoards()

        naval_battle.placeShips()













    elif op == 2:
        '''Vamos a ver si se llega a cargar el juego'''

    elif op == 3:
        print("Estás en AYUDA")
        print("Sólo puede haber dos jugadores: un jugador A y un jugador B.")
        print("Ambos dispondrán de dos tableros de 10 columnas por 10 filas:")
        print(f"\t-\tUn tablero POSICIÓN que le permitirá al jugador A posicionar sus barcos.")
        print(f"\t-\tUn tablero PRINCIPAL que les permitirá al jugador A disparar a los barcos del jugador B.")
        print("Los tipos de barcos que se pueden posicionar son cuatro:")
        print(f"\t-\tPortaaviones: ocupan 4 casilleros\t(cantidad disponible: 1)")
        print(f"\t-\t Submarinos: ocupan 3 casilleros\t(cantidad disponible: 1)")
        print(f"\t-\t Destructores: ocupan 2 casilleros\t(cantidad disponible: 1)")
        print(f"\t-\t Fragatas: ocupan 1 casillero\t\t(cantidad disponible: 2)")
        print("El juego se puede guardar y reanudarse en otro momento.")
        print(f"\nPresioná ENTER para volver atras.")

    elif op == 4:
        cycle_menu = False

    else:
        print("Has introducido un valor inválido.")
        op = editMenuOption()
