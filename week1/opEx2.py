def sao_multiplicaveis(m1, m2):
    l = 0
    for i in m2:
        l += len(i)
    return len(m1) == l
