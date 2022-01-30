# Exercício 1: Tamanho da matriz

Escreva uma função **dimensoes(matriz)** que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato **iXj**.

Exemplos:

```
minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)
# deve devolver 3X1
```

```
minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)
# deve devolver 2X3
```

# Exercício 2: Soma de matrizes

Escreva a função **soma_matrizes(m1, m2)** que recebe 2 matrizes e devolve uma matriz que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver **False**.

Exemplos:

```
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2)
# deve devolver [[3, 5, 7], [9, 11, 13]]
```

```
m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2)
# deve devolver False
```

# Exercício 1: Imprimindo matrizes

Como proposto na primeira vídeo-aula da semana, escreva uma função **imprime_matriz(matriz)**, que recebe uma matriz como parâmetro e imprime a matriz, linha por linha. **Note que NÃO se deve imprimir espaços após o último elemento de cada linha!**

Dica: lembre da primeira parte do curso, na semana 7! A função "print" em geral adiciona uma quebra de linha ao final, mas você pode controlar isso usando o argumento opcional "end"dessa forma:

```bash
>>>print("oi")
oi
>>>
>>>print("oi", end="")
oi>>>
```

Exemplos:

```bash
minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)
1
2
3
```

```bash
minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
1 2 3
4 5 6
```

# Exercício 2: Matrizes multiplicáveis

Duas matrizes são multiplicáveis se o número de colunas da primeira é igual ao número de linhas da segunda. Escreva a função **sao_multiplicaveis(m1, m2)** que recebe duas matrizes como parâmetro e devolve True se as matrizes forem multiplicavéis (na ordem dada) e False caso contrário.

Exemplos:

```bash
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
sao_multiplicaveis(m1, m2) => False
```

```bash
m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
sao_multiplicaveis(m1, m2) => True
```