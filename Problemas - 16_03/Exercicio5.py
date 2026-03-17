""" Leia quatro valores inteiros A, B, C e D.

Se B for maior do que C, D for maior do que A, a soma de C com D for maior que a soma de A e B, C e D forem positivos e A for par, escreva:

"Valores aceitos"

Caso contrário, escreva:

"Valores nao aceitos"

Entrada: quatro números inteiros em uma única linha.

Saída: a mensagem correspondente ao teste. Veja os exemplos abaixo. """
a, b, c, d = map(int, input().split())

if b > c and d > a and (c+d) > (a+b) and c > 0 and d > 0 and a%2==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")