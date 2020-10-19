#30mins
import time

#d(n) returns sum of proper divisors of n

sum_of_proper_divisors = {}
amicable_numbers = set()

def d(n):
	total = 0
	if n in sum_of_proper_divisors.keys():
		return sum_of_proper_divisors[n]

	for divisor in range(1,n//2+1):
		if n%divisor==0:
			total += divisor

	sum_of_proper_divisors[n] = total
	return sum_of_proper_divisors[n]

def amicable(a,b):

	if d(a) == b and d(b)==a:
		amicable_numbers.add(a)
		amicable_numbers.add(b)

start = time.time()


for a in range(2,10000):
	for b in range(2,10000):
		if a==b:
			continue
		amicable(a,b)

print(sum(amicable_numbers))


print(time.time()-start)