# 20mins

import time
from math import sqrt

def is_pentagonal(num):
	tmp = (sqrt(24 * num + 1) + 1) / 6
	return tmp == int(tmp)
start = time.time()
i = 1
isFound = False
while not isFound:
	p1 = i * (3 * i - 1) / 2
	for j in range(i - 1, 0, -1):
		p2 = j * (3 * j - 1) / 2
		if is_pentagonal(p1 + p2) and is_pentagonal(p1 - p2):
			isFound = True
			print (p1 - p2)
			break
	i += 1
print(time.time()-start)