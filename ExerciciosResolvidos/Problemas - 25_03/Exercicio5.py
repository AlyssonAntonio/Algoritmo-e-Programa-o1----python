i = 0
par, impar, n, p =0,0,0,0
while i<5:
    v=float(input())
    if v%2 == 0:
        par +=1
    else:
        impar+=1
    if  v>0:
        p+=1
    elif v<0:
        n+=1  
    i += 1

print(f"{par:.0f} valor(es) par(es)")
print(f"{impar:.0f} valor(es) impar(es)")
print(f"{p:.0f} valor(es) positivo(s)")
print(f"{n:.0f} valor(es) negativo(s)")