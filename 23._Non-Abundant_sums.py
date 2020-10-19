#22mins

import time

abundant_numbers = {}

def sum_of_proper_divisors(n):
	total = 0
	for x in range(1,n//2+1):
		if n%x==0:
			total += x
	return total

def fill_abundant():
	for n in range(2,28122):
		if sum_of_proper_divisors(n)>n:
			abundant_numbers[n] = sum_of_proper_divisors(n)


start = time.time()

fill_abundant()
ans = 0
for sum_of_numbers in range(28124):
	is_sum_of_abundant = False
	for i in range(sum_of_numbers):
		j = sum_of_numbers - i
		if (i in abundant_numbers.keys()) and (j in abundant_numbers.keys()):
			is_sum_of_abundant = True
			break
	if is_sum_of_abundant:
		continue
	elif not is_sum_of_abundant:
		ans += sum_of_numbers

print(ans)

print(time.time() - start)