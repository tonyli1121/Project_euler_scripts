# 40mins

from math import sqrt
import time

def generate_primes(limit):
    isprime = [True for i in range(limit+1)]
    for i in range(2,int(sqrt(limit))+1):
        if isprime[i]:
            for j in range(2*i,limit+1,i):
                isprime[j] = False
    return filter(lambda x:isprime[x],range(2,limit+1))

start = time.time()
primes =(list(generate_primes(1000000)))
print(len(primes))
longest = 0
maxx = 0
for x in range(4):
    total = 0
    length = longest
    for i in range(length):
        total+=primes[x+i]
    while total<1000000:
        total += primes[x+length]
        length += 1
        if total in primes:
            if length > longest:
                maxx = total
                longest = length

print(maxx)
print(time.time()-start)