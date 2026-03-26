""" tava em uma das questões do mentor mentor """
n = int(input())

binario = 0
multiplicador = 1

while n > 0:
    resto = n % 2
    binario += resto * multiplicador
    multiplicador *= 10
    n //= 2

print(binario)