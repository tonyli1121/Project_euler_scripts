# 8mins

import time
from math import sqrt

def is_triangle(num):
    tmp = (sqrt(8 * num + 1) - 1)/2
    return tmp == int(tmp)

def is_pentagonal(num):
    tmp = (sqrt(24 * num + 1) + 1) / 6
    return tmp == int(tmp)

start = time.time()
n = 143

while True:
    n+=1
    hexa = n*(2*n-1)
    if is_triangle(hexa) and is_pentagonal(hexa):
        print(hexa)
        break
print(time.time()-start)