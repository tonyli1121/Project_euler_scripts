#15mins
import time
from math import sqrt

def is_prime(num):
    if num<0:
        return False
    for x in range(2,int(sqrt(num)+1)):
        if num%x==0:
            return False
    return True

start = time.time()

ans = 1
longest = 0


for b in range(-1000,1001):
    if b>-41 and b<41:
        continue
    elif not is_prime(abs(b)):
        continue
    for a in range(-999,1000):
        n = 0
        length = 0
        while is_prime((n**2)+(a*n)+b):
            length+=1
            n+=1
        if length > longest:
            longest = length
            ans = a*b

            
print(ans)

print(time.time() - start)
