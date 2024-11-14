with open("./n.txt") as f:
    n=int(f.readline())
with open("./e.txt") as f:
    e=int(f.readline())
with open("./d.txt") as f:
    d=int(f.readline())
m=input('e or d')
if m=='e':
    x=int(input('x'))
    print(pow(x,e,n))
elif m=='d':
    x=int(input('x'))
    print(pow(x,d,n))
