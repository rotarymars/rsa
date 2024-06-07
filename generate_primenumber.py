import math
import os
import sys
args = sys.argv
a=int(args[1])
m=set()
f = open("./GeneratedPrime.txt","rb")
for i in f:
    m.add(int(i.rstrip()))
f.close()
#print(m)
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
m_list=sorted(m)
biggestprime=m_list[len(m_list)-1]
for i in range(biggestprime,biggestprime+a):
    isprime(i)
m_list=sorted(m)
f = open("./GeneratedPrime.txt",'w')
for i in m_list:
    f.write(str(i)+'\n')
#f.writelines(m)
f.close()
#print(m)
