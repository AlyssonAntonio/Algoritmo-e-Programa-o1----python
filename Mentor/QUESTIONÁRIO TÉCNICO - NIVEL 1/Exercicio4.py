""" O n-ésimo número harmônico é definido por

 
 
 

onde n > 0 é um inteiro.

Por exemplo, se n = 5 calculamos o 5º número harmônico da seguinte forma:

 
 
 
 


Faça um programa em Python 3 que leia um inteiro n > 0 e imprima o valor do n-ésimo número harmônico. O valor deve ser apresentado com 4 casas decimais.

Por exemplo:

Input	Resultado
2
1.5000
5
2.2833
10
2.9290
 """

# Step 1: Read the integer n
n = int(input())

# Step 2: Initialize harmonic sum
harmonic_sum = 0.0

# Step 3: Calculate the harmonic number
for i in range(1, n + 1):
    harmonic_sum += 1 / i

# Step 4: Print the result
print(f"{harmonic_sum:.4f}")