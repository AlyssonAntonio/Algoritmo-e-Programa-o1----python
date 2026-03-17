n1, n2, n3 = map(float, input().split())

media = (n1+n2+n3)/3

if media >= 6:
    print(f"Media: {media:.1f}")
    print("Aprovado.")
elif media >= 3.0 and media < 6.0:
    print(f"Media: {media:.1f}")
    print("Exame.")
else:
    print(f"Media: {media:.1f}")
    print("Reprovado.")