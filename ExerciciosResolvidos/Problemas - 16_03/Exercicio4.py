tam, queijo, borda = input().split()

total = 0

# tamanho da pizza
if tam == "P":
    total += 15.00
elif tam == "M":
    total += 18.50
else:
    total += 23.00

# adicional de queijo
if queijo == "S":
    if tam == "P":
        total += 2.50
    else:
        total += 4.00
# borda recheada
if borda == "S":
    total += 5.00

print(f"Total: R$ {total:.2f}")