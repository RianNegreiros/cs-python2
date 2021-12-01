def ordenada(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))
