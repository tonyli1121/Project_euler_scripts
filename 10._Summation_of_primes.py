#  sum of all the primes below two million.
# 5 mins but wrong(only 1 tiny mistake),23mins in total
import time
from math import sqrt

def IsPrime(num):
	for x in range(2,int(sqrt(num)+1)):
		if num%x==0:
			return False
	return True

start = time.time()
total = 0

for num in range(2,2000001):
	if IsPrime(num):
		total+=num


end = time.time()

print(total)
print(end-start)