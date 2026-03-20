""" Faça um programa em Python 3 que leia um número inteiro na base decimal e converta-o para a base binária. O número lido não deve ser convertido para string.

Por exemplo:

Input	Resultado
2
10
3
11
cornverter de valor decimal para binario
 """
n = int(input())

binario = 0
multiplicador = 1

while n > 0:
    resto = n % 2
    binario += resto * multiplicador
    multiplicador *= 10
    n //= 2

print(binario)