# 76mins

import time
from decimal import Decimal,getcontext

getcontext().prec = 2000

def digit_cycle(n):
	tmp = str(Decimal(1)/Decimal(n))
	tmp = tmp.replace('0.','')
	digits = []
	for x in range(len(tmp)):
		num_of_digits = 0
		
		if tmp[x] in digits:
			# y is the indices after tmp[x], tmp[x] not included
			letter_index = digits.index(tmp[x])
			num_of_digits +=1
			for y in range(1,len(digits) - letter_index):
				
				if (y == len(digits) - letter_index - 1) and (tmp[x+y] == digits[letter_index + y]):
					num_of_digits+=1
					return num_of_digits
				try:
					if tmp[x+y] == digits[letter_index + y]:
						num_of_digits += 1
						continue
					else:
						break
				except IndexError:
					break

		digits.append(tmp[x])
	
	return num_of_digits

start = time.time()


longest = 0
ans = 0
for n in range(2,1000):
	if digit_cycle(n)>longest:
		longest = digit_cycle(n)
		ans = n
	print(n)
print(ans)
print(time.time()-start)