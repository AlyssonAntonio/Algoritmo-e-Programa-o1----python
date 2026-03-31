""" Leia um valor inteiro N. Este valor representa a quantidade de casos de teste que virão a seguir.

Cada caso de teste é composto por três valores em ponto flutuante. Para cada um desses valores, calcule a média ponderada considerando que o primeiro valor tem peso 2, o segundo peso 3 e o terceiro peso 5.

Entrada: A primeira linha contém um inteiro N. Cada uma das N linhas seguintes contém três valores de ponto flutuante.

Saída: Para cada caso de teste, imprima a média ponderada com uma casa decimal.
 """


x = int(input())
i = 1
while i<=x:
    n1,n2,n3 = map(float, input().split())
    soma = (n1*2)+(n2*3)+(n3*5)
    print(f"{soma/10:.1f}")
    i+=1
    