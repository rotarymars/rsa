p=int(input())
q=int(input())
n=p*q
e=2
while True:
    if ((p-1)*(q-1))%e!=0:
        break
    e+=1
print('e',e)
d=1
while True:
    if d%1000000==0:
        print('d',d)
    if ((e*d)%((p-1)*(q-1)))==1:
        break
    d+=1
print('d',d)
