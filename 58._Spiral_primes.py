# 60mins

import time
from math import sqrt
'''
def gen_primes(limit):
    primes = [True for x in range(limit+1)]
    for i in range(2,int(sqrt(limit))+1):
        if primes[i]:
            for j in range(2*i,limit+1,i):
                primes[j] = False
    return filter(lambda x:primes[x], range(2,limit+1))

primes = list(gen_primes(1000000))    
'''

def is_prime(num):
    for i in range(3,int(sqrt(num))+1,2):
        if num%i == 0:
            return False
    return True


start = time.time()

length = 1
gap = 1
all_numbers = [1]
primes = []
perc = 1
while perc >= 0.1:
    length += 2
    for i in range(4):
        tmp = all_numbers[-1]+1+gap
        if is_prime(tmp):
            primes.append(tmp)
        all_numbers.append(tmp)
        
    perc = float(len(primes)/len(all_numbers))
    
    gap+=2
print(length)
print(time.time() - start)
