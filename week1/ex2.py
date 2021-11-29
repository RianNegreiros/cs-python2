from operator import add

def soma_matrizes(m1 , m2):
  i1 = len(m1)
  j1 = 0
  for t in m1:
    j1 = len(t)
  
  i2 = len(m2)
  j2 = 0
  for t in m2:
    j2 = len(t)
  
  if i1 == i2 and j1 == j2:
    m3 = list( map(add, m1[0], m2[0]))
    m4 = list( map(add, m1[1], m2[1]))
    return [m3, m4]
  else:
    return False