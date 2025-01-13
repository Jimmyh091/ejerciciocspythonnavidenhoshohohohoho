import random


def imprimir_arbol(filas):
    for it in range(1, filas + 1):
        print(" " * (filas - it) + "*" * it + "*" * (it - 1))

    # num = filas / 2 if filas % 2 == 0 else (filas - 1) / 2
    num = filas - 2

    print(" " * int(num) + "|||")


def filtrar_regalos(lista):
    return [x for x in lista if x[0] == 'R' or x[0] == 'r']


def contar_bolas(lista):
    return len([x for x in lista if x >= 5])


def sorteo_navidad(nombres, premios):
    resultados = []

    for it in range(0, len(premios) + 1):
        resultados.append("El premio " + random.choice(premios) + " es para " + random.choice(nombres))

    return resultados


def cuenta_regresiva(numero):
    it = numero

    while (it > 0):

        if it % 3 == 0 and it % 5 == 0:
            print(f"{it} = 😰")
        elif it % 3 == 0:
            print(f"{it} = 😂")
        elif it % 5 == 0:
            print(f"{it} = 🤣")
        else:
            print(f"{it} = 🗿")

        it -= 1


def sec_natal(lista):
    resultado = []

    for it in range(0, len(lista)):
        if lista[it][1] >= 18:
            resultado.append(lista[it][0])

    resultado.sort()
    print(resultado)
    return resultado


def comprobar_filas(tablero):
    for fila in tablero:

        for it in range(1, len(fila)):
            if fila[it] == fila[it - 1]:
                return False

    return True


def comprobar_columnas(tablero):
    for it in range(0, len(tablero)):

        for it2 in range(1, len(tablero)):
            if tablero[it][it2] == tablero[it][it2 - 1]:  # creo que it2 tiene que estar donde it1
                return False

    return True


def comprobar_cuadros(tablero):
    for itBig in range(0, len(tablero) / 3 - 1):
        for it2Big in range(0, len(tablero[0]) / 3 - 1):

            for itSmall in range(0, 2):
                for it2Small in range(0, 2):
                    tablero[itBig * 3 + itSmall][it2Big * 3 + it2Small] = 3


def coger_espacios(tablero):
    espacios = []

    for it in range(0, len(tablero)):
        for it2 in range(0, len(tablero[0])):

            if tablero[it][it2][1] == True:
                espacios.append([it, it2])

    return espacios


def trasformar_tablero(tablero):
    tablero_aux = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for it in range(0, len(tablero)):
        for it2 in range(0, len(tablero[0])):

            if tablero[it][it2] != 0:
                tablero_aux[it][it2] = [tablero[it][it2], False]
            else:
                tablero_aux[it][it2] = [1, True]

    return tablero_aux


def detransformar_sudoku(tablero):
    tablero_aux = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for it in range(0, len(tablero)):
        for it2 in range(0, len(tablero[0])):
            tablero_aux = tablero[it][it2][0]

    return tablero_aux


def funcion_backtracking(tablero, espacios):

    if comprobar_filas(tablero) and comprobar_columnas(tablero) and comprobar_cuadros(tablero):
        print("Resuelto")
    else:

        it = len(espacios) - 1

        while True:

            if tablero[espacios[it][0]][espacios[it][1]] == 9:
                tablero[espacios[it][0]][espacios[it][1]] = 1
            else:
                tablero[espacios[it][0]][espacios[it][1]] += 1

            if tablero[espacios[it][0]][espacios[it][1]] == 1:
                it -= 1
            else:
                break




def resolver_sudoku(tablero):
    print("Resolviendo sudoku...")

    tableroCopia = tablero.copy()


imprimir_arbol(50)
print(filtrar_regalos(["rafslkd", "skfdjha", "RsRkfdjae", "JKHkjfdase"]))
print(contar_bolas([4, 6, 7, 8, 2, 2, 2, 2, 7, 2, 2, 7, 2, 2, 26, 6, 27, 7823, 3]))
print(sorteo_navidad(["Jiame", "Jefferson", "Jimena", "JoJo"], ["GOTY", "Goya", "galardon de navidad"]))
cuenta_regresiva(50)
print(sec_natal(
    [["Jaime", 19], ["Gaspar", 103], ["Carlos", 12], ["Fran", 23], ["David", 29], ["Nacho", 17], ["Nahuel", 24]]))

resolver_sudoku(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
