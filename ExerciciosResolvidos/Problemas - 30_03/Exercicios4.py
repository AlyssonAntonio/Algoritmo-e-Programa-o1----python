""" Leia um valor inteiro N (1 ≤ N ≤ 10). A seguir, mostre a tabuada de N de 1 até 10.

Entrada: A entrada contém um valor inteiro N.

Saída: Imprima a tabuada de N de 1 até 10, conforme o formato mostrado nos exemplos. """

N  = int(input())
i=1
while i<=10:
    print(f"{i} x {N} = {N*i}")
    i+=1