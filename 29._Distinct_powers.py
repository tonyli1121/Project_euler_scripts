#2mins

import time

def generate_num(a,b):
	return a**b

start = time.time()

distinct_nums = set()

for a in range(2,101):
	for b in range(2,101):
		distinct_nums.add(generate_num(a,b))

print(len(distinct_nums))

print(time.time() - start)