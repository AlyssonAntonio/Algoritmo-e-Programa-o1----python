""" Leia um valor inteiro N. Este valor será a quantidade de valores inteiros que serão lidos em seguida.

Para cada valor lido, verifique se ele está dentro do intervalo [10,20] ou fora dele.

Ao final, mostre quantos valores estão dentro do intervalo e quantos estão fora.

Entrada: A primeira linha da entrada contém um inteiro N. As N linhas seguintes contêm um valor inteiro cada.

Saída: Imprima a quantidade de valores que estão dentro do intervalo e a quantidade de valores que estão fora do intervalo, conforme o formato mostrado nos exemplos.

Por exemplo:

Entrada	Resultado
4
14
123
10
-25
2 in
2 out
3
10
20
21
2 in
1 out
 """


##quantidade de valores inteiros que serão lidos
x = int(input())
i, dentro, fora = 1,0,0
while i <= x:
    v = int(input())

    if  10<= v <= 20:
        dentro += 1
    else:
        fora += 1
    i+=1
print(f"{dentro} in\n{fora} out")
