# 50mins

import time
from math import sqrt

def generate_primes(limit):
    isprimes = [True for i in range(limit+1)]
    for i in range(2,int(sqrt(limit))+1):
        if isprimes[i]:
            for j in range(2*i,limit+1,i):
                isprimes[j] = False
    return filter(lambda x:isprimes[x],range(2,limit+1))

start = time.time()

primes = set(generate_primes(10000))

num = 7
while True:
    num += 2
    isfound = False
    if num not in primes:
        for x in range(1,int(sqrt(num/2))+1):
            if (num - 2*x*x) in primes:
                isfound = True
        if not isfound:
            print(num)
            break

print(time.time()-start)