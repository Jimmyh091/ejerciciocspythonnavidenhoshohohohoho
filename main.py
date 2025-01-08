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

imprimir_arbol(50)
print(filtrar_regalos(["rafslkd", "skfdjha", "RsRkfdjae", "JKHkjfdase"]))
print(contar_bolas([4, 6, 7, 8, 2, 2, 2, 2, 7, 2, 2, 7, 2, 2, 26, 6, 27, 7823, 3]))
print(sorteo_navidad(["Jiame", "Jefferson", "Jimena", "JoJo"], ["GOTY", "Goya", "galardon de navidad"]))