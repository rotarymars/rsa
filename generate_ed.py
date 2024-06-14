def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
p=int(input())
q=int(input())
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
