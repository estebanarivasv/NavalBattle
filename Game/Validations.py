def editMenuOption():
    while True:
        try:
            option = int(input("Opción: "))
            return option
        except ValueError:
            print("No ingresaste un valor válido. Probá de nuevo.")


def editRowInfo():
    while True:
        try:
            row = int(input("Fila: "))
            return row
        except ValueError:
            print("No ingresaste un valor válido. Probá de nuevo.")


def editColumnInfo():
    while True:
        try:
            column = int(input("Columna: "))
            return column
        except ValueError:
            print("No ingresaste un valor válido. Probá de nuevo.")


def editOrientation():
    while True:
        orientation = input("Orientación (H - horizontal, V - vertical): ")
        if len(orientation) == 0:
            print("No ingresaste nada. Probá de nuevo.")
        else:
            orientation = orientation.upper()
            return orientation
