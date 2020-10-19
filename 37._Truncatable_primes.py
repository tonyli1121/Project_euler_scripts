# 15mins
import time
from math import sqrt

def truncatable(num):
    tmp = str(num)
    nums = []
    for x in range(len(tmp)-1):
        tmp = tmp[1:]
        nums.append(int(tmp))
    tmp = str(num)
    for x in range(len(tmp)-1):
        tmp = tmp[:-1]
        nums.append(int(tmp))
    return(nums)

def is_prime(num):
    if num == 1:
        return False
    for x in range(2,int(sqrt(num))+1):
        if not num%x:
            return False
    return True

def truncatable_primes(num):
    if not is_prime(num):
        return False
    for x in truncatable(num):
        if not is_prime(x):
            return False
    return True
        

start = time.time()

ans = 0
count = 0
num = 8
while count!=11:
    if truncatable_primes(num):
        ans += num
        count += 1
    num+=1
    
print(ans)

print(time.time()-start)