""" Leia um valor inteiro N. Este valor será a quantidade de valores inteiros que serão lidos em seguida.

Para cada valor lido, informe se o número é par ou ímpar. Além disso, informe se ele é positivo, negativo ou nulo.

Entrada: A primeira linha contém um inteiro N. As N linhas seguintes contêm um valor inteiro cada.

Saída: Para cada valor lido, imprima uma linha contendo a classificação do número conforme os exemplos. """

x = int(input())
i = 1
while i <= x:
    z = int(input())
    if z > 0 and z%2==0:
        print("EVEN POSITIVE")
    elif z > 0 and z%2!=0:
        print("ODD POSITIVE")
    elif z < 0 and z%2==0:
        print("EVEN NEGATIVE")
    elif z < 0 and z%2!=0:
        print("ODD NEGATIVE")
    elif z == 0:
        print("NULL")
    i+=1