from Boards import *
from Players import *
from Ships import *

def createGame():
    identifyPlayers()


def loadGame():
    pass

def help():
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

    print(f"\nIntroducí 1 para volver atras.")
    op = int(input("Opcion: "))
    if op == 1:
        menu()
    else:
        print("Has introducido un valor inválido.")