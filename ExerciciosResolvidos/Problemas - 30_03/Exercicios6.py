""" Leia 50 valores inteiros. Apresente então o maior valor lido e a posição dentre os 50 valores lidos.

Entrada: A entrada contém 50 números inteiros, um por linha.

Saída: Primeiro imprima o maior valor lido. Em seguida, na próxima linha, imprima a posição deste valor na sequência de entrada (considerando a primeira posição como 1).

Por exemplo:

Entrada	Resultado
12
7
98
34
56
23
45
67
89
10
3
5
8
21
14
39
40
41
42
43
44
46
47
48
49
50
51
52
53
54
55
57
58
59
60
61
62
63
64
65
66
68
69
70
71
72
73
74
75
76
98
3
 """

i=1
x,contador,v=0,1,0
while i<=50:
    x = int(input())
    if x > v:
        v = x
        contador=i
    i+=1
print(f"{v}\n{contador}")