# 30mins

import time
from math import sqrt

factors = {}

def num_of_factors(num):
    factors[num] = set()
    x = 2
    tmp = num
    while tmp!= 1:
        while not tmp % x:
            factors[num].add(x)
            tmp /= x
        if num!=tmp and tmp in factors.keys():
            factors[num] =  factors[num] | factors[tmp]
            break
        x+=1
    return len(factors[num])

start = time.time()

num = 2
ans = []
while len(ans)<4:
    if num_of_factors(num)==4:
        ans.append(num)
    else:
        ans = []
    num+=1
    
print(ans[0])
print(time.time()-start)
    