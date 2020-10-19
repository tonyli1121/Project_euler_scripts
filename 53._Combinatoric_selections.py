# 15mins
import time
from itertools import combinations

def factorial(num):
    tmp = 1
    for x in range(num,0,-1):
        tmp *= x
    return tmp

def combs(n,r):
    return (factorial(n)/(factorial(r)*factorial(n-r)))

start = time.time()
ans = 0

for n in range(1,101):
    for r in range(1,n+1):
        if combs(n,r)>=1000000:
            ans += 1

print(ans)
print(time.time()-start)