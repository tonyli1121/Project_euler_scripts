# 7mins

import time

def generate(digits):

    after_zeropoint = '0.'
    
    tmp = 1
    while True:
        if not len(after_zeropoint)<=digits+2:
            break
        after_zeropoint += str(tmp)
        tmp += 1
    return after_zeropoint

start = time.time()
num = generate(1000000)

ans = 1
print(num)
for x in range(7):
    ans *= int(num[10**x+1])
    
print(ans)

print(time.time()-start)
