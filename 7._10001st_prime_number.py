#40mins

import time

def isprime(num):
	# to determine if a num is a prime num, let num % 2 to num's sqrt,
	# if any of the results isn't 0, then the num is not a prime, else it is.
	for x in range(2,int(num**0.5)+1,1):
		if num%x == 0:
			return False
	return True

start = time.time()

rank = 1
num = 2
while rank!=10001:
	num+=1
	if isprime(num):
		rank+=1	
	
print(num)

end = time.time()
print(f'{end - start}s')
