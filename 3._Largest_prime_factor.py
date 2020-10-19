'''
initial method

def check_prime(num):
	count = 0
	for x in range(1,num+1):
		if not num%x:
			count+=1
	if count == 2:
		return True
	else:
		return False

def largest_prime_factor(num):
	
	for x in range(1,num+1):
		if check_prime(x) and not num%x:
			yield x

for x in largest_prime_factor(600851475143):
	print(x)

'''

def largest_prime_factor(num):
	factor = 2
	last_factor = 1
	while num>1:
		while num%factor == 0:
			last_factor = factor
			num = num/factor
		factor += 1
	return last_factor

print (largest_prime_factor(600851475143))