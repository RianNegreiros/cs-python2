def busca(lista, elemento):
    low = 0
    high = len(lista) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        print(mid)

        if lista[mid] < elemento:
            low = mid + 1

        elif lista[mid] > elemento:
            high = mid - 1

        else:
            return mid
    return False