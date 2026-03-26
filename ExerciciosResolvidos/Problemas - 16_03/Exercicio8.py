n1, n2 = map(int, input().split())

if n1 == 1:
    v1 = 4.00 * n2
elif n1 == 2:
    v1 = 4.50 * n2
elif n1 == 3:
    v1 = 5.00 * n2
elif n1 == 4:
    v1 = 2.00 * n2
elif n1 == 5:
    v1 = 1.50 * n2

print(f"Total: R$ {v1:.2f}")