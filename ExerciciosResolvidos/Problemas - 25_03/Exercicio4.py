i = 0
receba = 0
soma = 0
while i<5:
    v=float(input())
    if v%2 == 0:
        receba +=1
    i += 1
print(f"{receba:.0f} valores pares")