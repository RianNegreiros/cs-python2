# Exercício 1: Uma classe para triângulos

Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados **a**, **b** e **c** de um triângulo.

A classe triângulo também deve possuir um método **perimetro**, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.

```
t = Triangulo(1, 1, 1)
# deve atribuir uma referência para um triângulo de lados 1, 1 e 1 à variável t 
```

Um objeto desta classe deve responder às seguintes chamadas:

```
t.a
# deve devolver o valor do lado a do triângulo
t. b
# deve devolver o valor do lado b do triângulo
t.c
# deve devolver o valor do lado c do triângulo

t.perimetro()
# deve devolver um inteiro correspondente ao valor do perímetro do triângulo.
```

# Exercício 2: Tipos de triângulos

Na classe triângulo, definida na Questão 1, escreva o metodo **tipo_lado()** que devolve uma string dizendo se o triângulo é:

**isósceles** (dois lados iguais)

**equilátero** (todos os lados iguais)

**escaleno** (todos os lados diferentes)

Note que se o triângulo for equilátero, a função **não** deve devolver isóceles.

Exemplos:

```bash
t = Triangulo(4, 4, 4)
t.tipo_lado()
# deve devolver 'equilátero'

u = Triangulo(3, 4, 5)
.tipo_lado()
# deve devolver 'escaleno'
```

# Exercício 1: Triângulos retângulos

Escreva, na classe Triangulo, o método **retangulo()** que devolve **True** se o triângulo for retângulo, e **False** caso contrário.

Exemplos:

```bash
t = Triangulo(1, 3, 5)
t.retangulo()
# deve devolver False

u = Triangulo(3, 4, 5)
u.retangulo()
# deve devolver True
```

#Exercício 2: Triângulos semelhantes

Ainda na classe **Triangulo**, escreva um método **semelhantes(triangulo)** que recebe um objeto do tipo **Triangulo** como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve devolver **True**. Caso negativo, deve devolver **False**

Um triângulo é semelhante a outro triângulo se a razão (divisão) entre os comprimentos dos seus lados forem iguais.

**Dica**: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.

Exemplo:

```bash
t1 = Triangulo(2, 3, 5)
t2 = Triangulo(4, 6, 10)
t1.semelhantes(t2)
# deve devolver True
```