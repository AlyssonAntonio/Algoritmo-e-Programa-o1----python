""" N = int(input())
i = 1
while i<=N:
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)
    i+=1
 """

N = int(input())
i = 1
for i in range(1, N+1):
     if i%3==0 and i%5==0:
        print("FizzBuzz")
     elif i%3==0:
        print("Fizz")
     elif i%5==0:
        print("Buzz")
     else:
        print(i)
   