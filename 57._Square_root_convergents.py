# 10mins
import time

def count_digit(num):
    return len(str(num))

start = time.time()

num = [3]
den = [2]
ans = 0
for index in range(1000):
    den.append(num[index] + den[index])
    num.append(den[index] + den[index+1])
    if count_digit(num[index+1]) > count_digit(den[index+1]):
        ans += 1
    
print(ans)
print(time.time() - start)