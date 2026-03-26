i = 0
receba = 0
while i<6:
    v=float(input())

    if v > 0:
        receba +=1
    i += 1
print(f"{receba:.0f} valores positivos")