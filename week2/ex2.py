def menor_nome(nomes):
    nm = []
    for i in nomes:
        j = i.replace(' ', '')
        nm.append(j)
    nm.sort(key=len)
    return nm[0].capitalize()
