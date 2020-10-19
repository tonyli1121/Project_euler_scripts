# 45
# 2 mins
import time

def get_digit(num):
    return(len(str(num)))

start = time.time()

ans = 0

for base in range(1,10):
    for n in range(1000):
        if get_digit(base**n) == n:
            ans += 1
            
print(ans)
print(time.time() - start)