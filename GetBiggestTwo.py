def returnbiggesttwo()->[int]:
    primelist=[]
    with open("./GeneratedPrime.txt") as f:
        primelist=[s.rstrip() for s in f.readlines()]
    print(primelist.pop(),primelist.pop())
    return int(primelist.pop()),int(primelist.pop())
