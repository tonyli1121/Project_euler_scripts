# 8mins

import time

start = time.time()

ans = '10405071317'

for num in range(11,1000):# 1000 is useless because it ends with 0000000
    ans = str((int(ans[-11:]) + int(str(num**num)[-11:]))) # used -11 as index just in case index -10 of both ans and num**num are zeroes
    
print(ans[-10:])

print(time.time()-start)