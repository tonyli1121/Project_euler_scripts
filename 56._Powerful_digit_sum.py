#3mins
import time

def sum_of_digits(num):
    tmp = str(num)
    ans = 0
    for digit in tmp:
        ans += int(digit)
    return ans

start = time.time()

ans = 0
for a in range(2,100):
    for b in range(2,100):
        ans = max(ans,sum_of_digits(a**b))

print(ans)
print(time.time()-start)