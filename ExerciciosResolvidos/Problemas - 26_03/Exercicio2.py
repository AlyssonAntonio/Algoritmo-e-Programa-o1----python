x=int(input())
dec=0
pot=0
while x>0:
    receba = x %10
    dec+=receba*(2**pot)
    x = x//10
    pot += 1
print(dec)