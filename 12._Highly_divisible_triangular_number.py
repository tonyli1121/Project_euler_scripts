# 12mins 暴力求解 时间过长
# 上网找到例解，求factor皆用sqrt 用时5s左右

import time
from math import sqrt
start = time.time()

num = 1
plus = 2
found = False
while True:
	factor_num = 0
	if int(sqrt(num)) == sqrt(num):
		factor_num -=1
	for x in range(1,int(sqrt(num))+1):
		if num%x==0:
			factor_num+=2
		if factor_num>500:
			found = True
			break

	if found:
		break

	num += plus
	plus += 1

print (num)

end = time.time()
print(end-start)