""" Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N se for o caso.

Entrada: A entrada contém um valor inteiro N.

Saída: Para cada valor par entre 1 e N, imprima uma linha no formato i^2 = X, onde i é o número par e X é o seu quadrado.

Por exemplo:

Entrada	Resultado
6
2^2 = 4
4^2 = 16
6^2 = 36
3
2^2 = 4

 """
N = int(input())
i = 2
while i <= N:
    print(f"{i}^2 = {i*i}")
    i += 2

