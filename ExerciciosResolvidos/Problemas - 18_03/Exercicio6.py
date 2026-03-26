""" Leia três valores de ponto flutuante A, B e C.

Ordene os valores em ordem decrescente de modo que A seja o maior dos três.

Com base nos valores ordenados, determine o tipo de triângulo:

Se A ≥ B + C, escreva: NAO FORMA TRIANGULO

Se A² = B² + C², escreva: TRIANGULO RETANGULO

Se A² > B² + C², escreva: TRIANGULO OBTUSANGULO

Se A² < B² + C², escreva: TRIANGULO ACUTANGULO

Se os três lados forem iguais, escreva: TRIANGULO EQUILATERO

Se apenas dois lados forem iguais, escreva: TRIANGULO ISOSCELES

Entrada: três números reais.

Saída: uma ou mais classificações, exatamente conforme especificado acima.

Por exemplo:

Entrada	Resultado
7.0 5.0 7.0
TRIANGULO ACUTANGULO
TRIANGULO ISOSCELES
6.0 6.0 10.0
TRIANGULO OBTUSANGULO
TRIANGULO ISOSCELES """

A, B, C = map(float, input().split())

if A < B:
    A, B = B, A
if A < C:
    A, C = C, A
if B < C:
    B, C = C, B

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")