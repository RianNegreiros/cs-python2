def ordena(lista):
    n = len(lista)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if lista[j] < lista[m]:
                m = j
        lista[i], lista[m] = lista[m], lista[i]
    return lista
