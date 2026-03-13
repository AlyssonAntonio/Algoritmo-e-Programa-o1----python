Dindin = int(input())
#Considere as seguintes cédulas: 100, 50, 20, 10, 5, 2 e 1.
receba = Dindin
v1 = Dindin // 100
Dindin = Dindin%100
v2 = Dindin // 50
Dindin = Dindin%50
v3 = Dindin // 20
Dindin = Dindin%20
v4 = Dindin // 10
Dindin = Dindin%10
v5 = Dindin // 5
Dindin = Dindin%5
v6 = Dindin // 2
Dindin = Dindin%2
v7 = Dindin // 1
Dindin = Dindin%1

#Considere as seguintes cédulas: 100, 50, 20, 10, 5, 2 e 1.
print(receba)
print(f"{v1} nota(s) de R$ 100,00\n{v2} nota(s) de R$ 50,00\n{v3} nota(s) de R$ 20,00\n{v4} nota(s) de R$ 10,00\n{v5} nota(s) de R$ 5,00\n{v6} nota(s) de R$ 2,00\n{v7} nota(s) de R$ 1,00")