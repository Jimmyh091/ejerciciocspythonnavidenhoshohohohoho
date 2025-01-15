import random
import sys


def espaciar():
    for it in range(0, 3):
        print("")


def imprimir_arbol(filas):
    print(f"\n\nEjercicio 1: Arbol de {filas} filas\n")

    for it in range(1, filas + 1):
        print(" " * (filas - it) + "*" * it + "*" * (it - 1))

    num = filas - 2

    print(" " * int(num) + "|||")

    espaciar()


def filtrar_regalos(lista):
    print("Ejercicio 2: Filtrar regalos introducidos\n")

    print(f"Regalos: {lista}"
          .replace("[", "").replace("]", "").replace("'", ""))

    regalos_filtrados = [x for x in lista if x[0] == 'R' or x[0] == 'r']

    print(f"Regalos que empiecen con R: {lista}"
          .replace("[", "").replace("]", "").replace("'", ""))

    espaciar()


def contar_bolas(lista):
    print("Ejercicio 3: Contar bolas de nieve > 5\n")

    print(f"Tamanho de las bolas: {lista}"
          .replace("[", "").replace("]", ""))

    bolas_filtradas = len([x for x in lista if x >= 5])

    print(f"Cantidad de bolas > 5: {bolas_filtradas}"
          .replace("[", "").replace("]", ""))

    espaciar()


def sorteo_navidad(nombres, premios):
    print("Ejercicio 4: Otorgar premios aleatoriamente\n")

    print(f"Nominados: {nombres}"
          .replace("[", "").replace("]", "").replace("'", ""))
    print(f"Premios: {premios}\n"
          .replace("[", "").replace("]", "").replace("'", ""))

    resultados = []

    for it in range(0, len(premios) + 1):
        resultados.append("El premio " + random.choice(premios) + " es para " + random.choice(nombres))

    print(f"Resultados: {resultados}"
          .replace("[", "").replace("]", "").replace("'", ""))

    espaciar()


def cuenta_regresiva(numero):
    print("Ejercicio 5: Cuenta regresiva y dividendos de 3 y/o 5\n")

    it = numero

    while it > 0:

        if it % 3 == 0 and it % 5 == 0:
            print(f"{it} = 🎁")
        elif it % 3 == 0:
            print(f"{it} = 🎆")
        elif it % 5 == 0:
            print(f"{it} = 🎄")

        it -= 1

    espaciar()


def sec_natal(lista):
    resultado = []

    for it in range(0, len(lista)):
        if lista[it][1] >= 18:
            resultado.append(lista[it][0])

    resultado.sort()
    print(resultado)
    return resultado


# Sudoku

def comprobar_filas(tablero):
    for it in range(0, len(tablero)):
        for it2 in range(1, len(tablero[0])):

            if tablero[it][it2][0] == tablero[it][it2 - 1][0]:
                return False

    return True


def comprobar_columnas(tablero):
    for it in range(0, len(tablero)):
        for it2 in range(1, len(tablero)):
            if tablero[it][it2][0] == tablero[it][it2 - 1][0]:  # creo que it2 tiene que estar donde it1
                return False

    return True


def comprobar_cuadros(tablero):
    for itBig in range(0, int(len(tablero) / 3 - 1)):
        for it2Big in range(0, int(len(tablero[0]) / 3 - 1)):

            lista_nums = []

            for itSmall in range(0, 3):
                for it2Small in range(0, 3):

                    if tablero[itBig * 3 + itSmall][it2Big * 3 + it2Small][0] in lista_nums:
                        return False
                    else:
                        lista_nums.append(tablero[itBig * 3 + itSmall][it2Big * 3 + it2Small][0])

    return True


def coger_espacios(tablero):
    espacios = []

    for it in range(0, len(tablero)):
        for it2 in range(0, len(tablero[0])):

            if tablero[it][it2][1]:
                espacios.append([it, it2])

    return espacios


def transformar_tablero(tablero):
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


def detransformar_tablero(tablero):
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
            tablero_aux[it][it2] = tablero[it][it2][0]

    return tablero_aux


def funcion_backtracking(tablero, espacios):
    if comprobar_filas(tablero) and comprobar_columnas(tablero) and comprobar_cuadros(tablero):
        return tablero
    else:

        it = len(espacios) - 1

        while True:

            if tablero[espacios[it][0]][espacios[it][1]][0] == 9:
                tablero[espacios[it][0]][espacios[it][1]][0] = 1
            else:
                tablero[espacios[it][0]][espacios[it][1]][0] += 1

            if tablero[espacios[it][0]][espacios[it][1]][0] == 1:
                it -= 1
            else:
                break

        return funcion_backtracking(tablero, espacios)


def resolver_sudoku(tablero):

    tableroCopia = transformar_tablero(tablero)

    espacios = coger_espacios(tableroCopia)

    print(f"Ejercicio 6: Sudoku con {len(espacios)} espacios")

    resultado = detransformar_tablero(funcion_backtracking(tableroCopia, espacios))

    for fila in resultado:
        print(fila)


# Colocar Reina

def colocar_diagonal_izqsup_derinf(tablero, x, y):
    xaux = x
    yaux = y

    while xaux > 0 and yaux > 0:
        xaux -= 1
        yaux -= 1

    while xaux < len(tablero) and yaux < len(tablero):
        tablero[xaux][yaux] = 1

        xaux += 1
        yaux += 1


def colocar_diagonal_dersup_izqinf(tablero, x, y):
    xaux = x
    yaux = y

    while xaux < len(tablero) - 1 and yaux > 0:
        xaux += 1
        yaux -= 1

    while xaux >= 0 and yaux < len(tablero):
        tablero[xaux][yaux] = 1

        xaux -= 1
        yaux += 1


def colocar_reina(tablero, x, y):
    # comprobar vertical y horizontal
    for it in range(0, len(tablero)):
        for it2 in range(0, len(tablero)):

            if it == x:
                tablero[it][it2] = 1
            elif it2 == y:
                tablero[it][it2] = 1

    colocar_diagonal_izqsup_derinf(tablero, x, y)
    colocar_diagonal_dersup_izqinf(tablero, x, y)


def resolver_n_reinas(filas):
    filas -= 1

    tablero = []
    posiciones = []

    for it in range(0, filas + 1):

        fila = []

        for it2 in range(0, filas + 1):
            fila.append(0)

        tablero.append(fila)

    for it in range(0, len(tablero)):
        for it2 in range(0, len(tablero)):

            if tablero[it][it2] == 0:
                posiciones.append([it, it2])
                colocar_reina(tablero, it, it2)
                tablero[it][it2] = 8

    for it in tablero:
        print(it)

    return posiciones


imprimir_arbol(6)

filtrar_regalos(["rafslkd", "skfdjha", "RsRkfdjae", "JKHkjfdase"])

contar_bolas([4, 6, 7, 8, 2, 2, 2, 2, 7, 2, 2, 7, 2, 2, 26, 6, 27, 7823, 3])

sorteo_navidad(["Jiame", "Jefferson", "Jimena", "JoJo"], ["GOTY", "Goya", "galardon de navidad"])

cuenta_regresiva(50)

sec_natal([["Jaime", 19], ["Gaspar", 103], ["Carlos", 12], ["Fran", 23], ["David", 29], ["Nacho", 17], ["Nahuel", 24]])

# Necesario para poder calcular muchos espacios
# sys.setrecursionlimit(999999999)
resolver_sudoku(

    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
)
resolver_n_reinas(5)
# prueba
# [
#         [5, 3, 4, 6, 7, 8, 9, 1, 2],
#         [6, 7, 2, 1, 9, 5, 3, 4, 8],
#         [1, 9, 8, 3, 4, 2, 5, 6, 7],
#         [8, 5, 9, 7, 6, 1, 4, 2, 3],
#         [4, 2, 6, 8, 5, 3, 7, 9, 1],
#         [7, 1, 3, 9, 2, 4, 8, 5, 6],
#         [9, 6, 1, 5, 3, 7, 2, 8, 4],
#         [2, 8, 7, 4, 1, 9, 6, 3, 5],
#         [3, 4, 5, 2, 8, 6, 1, 7, 9],
#     ]
