from random import randint


def lista_grande(n):
    lista = []
    while len(lista) < n:
        lista.append(randint(1, 1000))
    return lista