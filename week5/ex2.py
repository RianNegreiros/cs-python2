def bubble_sort(lista):
    m = len(lista)

    for i in range(len(lista)):
        for j in range(0, m-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
    return lista