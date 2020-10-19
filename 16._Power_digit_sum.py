# 3mins
# sum of the digits of 2**1000

import time
start = time.time()

num = str(2**1000)
ans = 0
for i in range(len(num)):
	ans += int(num[i])

print(ans)
print(time.time()- start)