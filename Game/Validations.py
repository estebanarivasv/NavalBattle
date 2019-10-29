def editRowInfo():
    while True:
        try:
            row = int(input("Fila: "))
            return row
        except ValueError:
            print("No ingresaste nada. Probá de nuevo.")


def editColumnInfo():
    try:
        column = int(input("Columna: "))
        return column
    except ValueError:
        print("No ingresaste nada. Probá de nuevo.")


def editOrientation():
    orientation = input("Orientación (H - horizontal, V - vertical): ")
    if len(orientation) == 0:
        print("No ingresaste nada. Probá de nuevo.")
        editOrientation()
    else:
        orientation = orientation.upper()
        return orientation
