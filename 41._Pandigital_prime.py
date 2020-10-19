# 56mins

import time
from math import sqrt

def pandigital(num):
    tmp = ''
    for x in range(1,len(str(num))+1):
        tmp += str(x)
    
    return ''.join(sorted(str(num))) == tmp

def is_prime(num):
    for x in range(2,int(sqrt(num))+1):
        if not num%x:
            return False
    return True

def generate_primes(limit):
    
    prime = [ True for i in range(limit+1) ]
    
    for x in range(2,int(sqrt(limit))+1):
        if prime[x]:
            for j in range(x**2,limit+1,x):
                prime[j] = False
        
    return filter(lambda x:prime[x],range(limit,1,-1))

start = time.time()

prime_nums = generate_primes(7654321)

for x in prime_nums:
    if pandigital(x):
        ans = x
        break
    
print(ans)

print(time.time() - start)
