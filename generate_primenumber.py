import math
import GetBiggestTwo
import os
import sys
import time
args = sys.argv
a=int(args[1])
m=set()
start=time.time()
f = open("./GeneratedPrime.txt","rb")
for i in f:
    m.add(int(i.rstrip()))
f.close()
#print(m)
end=time.time()
print(f"Used {end-start} secs to read generated prime numbers")
def isprime(a: int) -> bool: 
    global m
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
start=time.time()
m_list=sorted(m)
biggestprime=m_list[len(m_list)-1]
for i in range(biggestprime,biggestprime+a):
    if isprime(i):
        print(i)
end=time.time()
print(f"{(end-start)/a} sec per number.")
start=time.time()
m_list=sorted(m)
f = open("./GeneratedPrime.txt",'w')
for i in m_list:
    f.write(str(i)+'\n')
#f.writelines(m)
f.close()
#print(m)
end=time.time()
print(f"Used {end-start} secs to write prime numbers")
first, second=GetBiggestTwo.returnbiggesttwo()
f=open("./n.txt",'w')
f.write(str(first*second))
f.close()

