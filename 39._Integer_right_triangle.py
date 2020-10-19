# 50mins
import time
from math import sqrt
# right angle triangle with integral length sides, {a,b,c}
# a**2 + b**2 == c**2
# c = p - (a + b) 
# a <= b < c
# 
# a max: a = b
# 2*a^2 = c^2 = (p - 2a)^2
# a max: (sqrt(2)+2)a = p
# a <= p/(sqrt(2)+2)
# 1 , int(p//(sqrt(2)+2))+1



start = time.time()

maxi = 0
ans = 0

for p in range(1,1001):
    count = 0
    for a in range(1,int(p//(sqrt(2)+2))+1): 
        for b in range(a,((p-a)//2)+1):
            c = p - a - b
            if a**2+b**2== c**2:
                count += 1
    if count>maxi:
        maxi = count
        ans = p
        
print (ans)
    
print(time.time() - start)