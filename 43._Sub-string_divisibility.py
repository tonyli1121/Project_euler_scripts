#30mins

import time
from itertools import permutations

start = time.time()

numbers = [''.join(i) for i in permutations('0123456789')]

ans = 0

for x in numbers:
    if x[0] == '0':
        continue
    if int(x[1:4])%2:
        continue
    if int(x[2:5])%3:
        continue
    if int(x[3:6])%5:
        continue
    if int(x[4:7])%7:
        continue
    if int(x[5:8])%11:
        continue
    if int(x[6:9])%13:
        continue
    if int(x[7:10])%17:
        continue
    ans += int(x)

print(ans)
print(time.time()-start)