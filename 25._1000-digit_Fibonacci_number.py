# 6mins

import time
start = time.time()

a = 1
b = 1
count = 2
while True:
	tmp = b
	b = a+b
	a = tmp
	count+=1
	if len(str(b))==1000:
		print(count)
		break

print(time.time()-start)