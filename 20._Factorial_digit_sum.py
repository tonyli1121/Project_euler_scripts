# 3mins
# 100! = 1x2x3x4x...x100
# find sum of digits of 100!

import time

def factorial(num):
	tmp = 1
	for x in range(1,num+1):
		tmp *= x
	return str(tmp)

start = time.time()

ans = 0

for num in factorial(100):
	ans += int(num)

print(ans)

print(time.time() - start)