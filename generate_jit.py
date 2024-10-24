import re

# サンプルコード
sample_code = '''
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


'''

# JITコンパイルを追加する関数
def add_jit_to_code(code):
    # 関数の定義を見つけるための正規表現パターン
    function_pattern = re.compile(r'def (\w+)\((.*?)\):')
    
    # JITデコレータを追加するためのコード
    jit_code = '@jit(nopython=True)\n'
    
    # 関数名と引数を取得
    def replace_function_definition(match):
        function_name = match.group(1)
        args = match.group(2)
        return f'{jit_code}def {function_name}({args}):'
    
    # コードにJITデコレータを追加
    new_code = function_pattern.sub(replace_function_definition, code)
    
    return new_code

# ジェネレートされたJITコードを表示
print("元のコード:")
print(sample_code)

jit_code = add_jit_to_code(sample_code)
print("\nJITコンパイル後のコード:")
print(jit_code)
