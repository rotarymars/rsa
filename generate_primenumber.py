import math
a=int(input("bigger than:"))
b=int(input("less than:"))
m=set()
def isprime(a: int) -> bool: 
    biggestprimeinm=2
    for i in m:
        if a <= i:
            continue
        if a % i == 0:
            return False
        biggestprimeinm=max(biggestprimeinm,i)
    for i in range(biggestprimeinm, int(math.sqrt(a))+1):
        if isprime(i):
            m.add(i)
        if a % i == 0:
            return False
    m.add(a)
    return True
for i in range(a,b+1):
    if isprime(i):
        print(i)
print(m)
