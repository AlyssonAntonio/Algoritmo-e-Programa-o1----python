salario = float(input())

if  salario <= 400:
    reajuste = salario* 0.15
    salario = salario+reajuste
    print(f"Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 15 %")
elif 400.01 <= salario <= 800:
    reajuste = salario* 0.12
    salario = salario+reajuste
    print(f"Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 12 %")
elif 800.01 <= salario <= 1200.00:
    reajuste = salario* 0.10
    salario = salario+reajuste
    print(f"Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 10 %")
elif 1200.01 <= salario <= 2000:
    reajuste = salario* 0.07
    salario = salario+reajuste
    print(f"Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 7 %")
else:
    reajuste = salario* 0.04
    salario = salario+reajuste
    print(f"Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 4 %")