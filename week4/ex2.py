def busca(lista, elemento):
  pos = 0
  encon = False
  while pos < len(lista) and not encon:
    if lista[pos] == elemento:
      encon = True
      return pos
    else:
      pos += 1
  return encon