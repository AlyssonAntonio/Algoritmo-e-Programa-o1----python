n, x = map(int, input().split())
i, sorte = 1,0 
while i <= n:
    valores = int(input())
    if valores == x:
        sorte += 1
    i+=1

if sorte > 0:
    print("Sorte")
else:
    print("Azar")