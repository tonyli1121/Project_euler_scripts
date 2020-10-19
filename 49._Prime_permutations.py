# 68mins

import time
from math import sqrt
from itertools import permutations

def perms(num):
    pers = list(permutations(str(num)))
    for i in range(len(pers)):
        pers[i] = int(''.join(pers[i]))
    return set(pers)
    

def generate_primes(limit):
    isprime = [True for i in range(limit+1)]
    for i in range(2,int(sqrt(limit))+1):
        if isprime[i]:
            for j in range(2*i,limit+1,i):
                isprime[j] = False
    return filter(lambda x:isprime[x],range(2,limit+1))

start = time.time()

primes = list(generate_primes(10000))
print(primes)
isfound = False
for x in range(1488,10000):  
    if x not in primes:
        continue
    ans = ''
    l = list(filter(lambda x:x in primes,perms(x)))# perms, primes
    l.sort()
    if x in l:
        l.remove(x)
    # arithmetic_sequence
    print(l)
    if len(l)>=3:
        for i in range(len(l)):
            for j in range(i,len(l)):
                if abs(l[j] - l[i]) == l[i] - x:
                    isfound = True
                    ans += str(x) + str(l[i]) + str(l[j])
                    break
            if isfound:
                break
        if isfound:
            break

print(ans)
print(time.time()-start)
