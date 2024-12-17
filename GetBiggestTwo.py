import re
import os
def returnbiggesttwo()->[int]:
    primelist=[]
    for i in os.listdir():
        if re.match("GeneratedPrime_[0-9]+.txt",i):
            with open(i) as f:
                primelist=[s.rstrip() for s in f.readlines()]
    primelist=sorted(primelist)
    return int(primelist.pop()),int(primelist.pop())
