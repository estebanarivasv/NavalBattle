import Boards
import Ships
import Game

def menu():
    print("Seleccioná una opción para continuar:")
    print(f"1.\tCrear partida", f"\n2.\tCargar partida guardada", f"\n3.\tAyuda", f"\n4.\tSalir")
    op = int(input("Opción: "))
    if op == 1:
        createGame()
    elif op == 2:
        loadGame()
    elif op == 3:
        help()
    elif op == 4:
        pass
    else:
        print("Has introducido un valor inválido.")

"""MAIN"""
print("¡Bienvenido a Naval Battle Game!")
menu()
