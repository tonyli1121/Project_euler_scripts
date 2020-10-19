# 57

import time

def fifth_power_digits(n):
	tmp = str(n)
	total = 0 
	for digit in tmp:
		total += int(digit)**5
	return total

start = time.time()
ans = 0
for x in range(2,1000000):
	if x == fifth_power_digits(x):
		ans+=x
print(ans)
print(time.time()-start)