v1, v2, v3 = map(int, input().split())
sla1,sla2 ,sla3 = v1, v2, v3 

if v1 > v2:
    v1, v2 = v2, v1
if v1 > v3:
    v1, v3 = v3, v1
if v2 > v3:
    v2, v3 = v3, v2

print(v1)
print(v2)
print(v3)
print()
print(sla1)
print(sla2)
print(sla3)