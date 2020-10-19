# sum of 1~100's total's square - 1~100 square's sum
# 3mins

import time
start = time.time()

sum_square = 0
square_of_sum = 0
for x in range(1,101):
	sum_square += x**2
for x in range(1,101):
	square_of_sum += x
square_of_sum = square_of_sum**2
print(square_of_sum - sum_square)

end = time.time()
print(f'{end - start}s')