from math import sqrt
from itertools import product
import time

def gen_primes(limit):
    is_prime = [True for x in range(limit+1)]
    for i in range(2,int(sqrt(limit))+1):
        if is_prime[i]:
            for j in range(i**2,limit+1,i):
                is_prime[j] = False
    return filter(lambda x:is_prime[x],range(2,limit+1))

primes = set(gen_primes(1000000))

def count_prime_w_replacement(num,digit):
    count = 0
    for c in range(0,10):
        tmp = num.replace(digit,str(c))
        if tmp[0] != '0' and int(tmp) in primes:
            count+=1
    return count

start = time.time()

ans = 1000000
for p in primes:
    num = str(p)
    for c in range(0,3):
        if num.count(str(c)) == 3 and count_prime_w_replacement(num,str(c))>7:
            ans = min(ans,p)
            
print (ans)
print(time.time() - start)