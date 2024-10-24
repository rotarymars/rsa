import os
from GetBiggestTwo import returnbiggesttwo
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
p,q=returnbiggesttwo()
n=p*q
print('n',n)
e=2
tmp=(p-1)*(q-1)
while True:
    if tmp%e!=0:
        break
    e+=1
print('e',e)
d=1
temp=0
while True:
    if (tmp*temp+1)%e==0:
        d=(tmp*temp+1)//e
        break
    temp+=1
print('d',d)
with open("./n.txt",mode='w') as f:
    f.write(f"{str(n)}\n")
with open("./e.txt",mode='w') as f:
    f.write(f"{str(e)}\n")
with open("./d.txt",mode='w') as f:
    f.write(f"{str(d)}\n")
