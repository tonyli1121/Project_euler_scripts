# 27mins got the right code, but took much longer to solve as i used 100,000 instead of 1,000,000

import time
from math import sqrt

def is_prime(num):
    for x in range(2,int(sqrt(num))+1):
        if num % x == 0:
            return False
    return True

def circular(num):
    digits = [x for x in str(num)]
    # tmp = [0] [0] = [1] [1] = [2] [2] = [3]
    circs = []
    for times in range(len(str(num))-1):
        tmp = digits[0]
        for i in range(len(str(num))-1):
            digits[i] = digits[i+1]
        digits[-1] = tmp
        circs.append(int(''.join(digits)))
    return circs

start = time.time()

circular_primes = set([2,3,5,7])

for x in range(2,1000000):
    count = 0
    all_primes = False
    #--------------
    if not is_prime(x):
        continue
    if x in circular_primes:
        continue
    #---------------
    for i in circular(x):
        if not is_prime(i):
            break
        count += i
        if count == sum(circular(x)):
            all_primes = True
    if all_primes:
        circular_primes.add(x)
        for i in circular(x):
            circular_primes.add(i)

#--------------------
l = list(circular_primes)
l.sort()
print(l)

print(len(l))

print(time.time()-start)