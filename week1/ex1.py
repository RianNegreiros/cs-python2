def dimensoes(matriz):
  i = len(matriz)
  j = 0
  for t in matriz:
    j = len(t)
  print(str(i) + "X" + str(j))