i = 0
receba = 0
soma = 0
while i<6:
    v=float(input())
    if v > 0:
        receba +=1
        soma = soma + v
    i += 1
media = soma/receba
print(f"{receba:.0f} valores positivos")
print(f"{media:.1f}")