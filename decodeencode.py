n=int(input('n'))
e=int(input('e'))
d=int(input('d'))
m=input('e or d')
if m=='e':
    x=int(input('x'))
    print(pow(x,e,n))
elif m=='d':
    x=int(input('x'))
    print(pow(x,d,n))
