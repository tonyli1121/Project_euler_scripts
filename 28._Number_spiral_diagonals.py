import time

start = time.time()

def spiral_diagonal(n):
	n -= 1
	ret = 1
	num = 1
	add = 2
	for i in range(0, n//2):
		ret += num * 4 + add * 10
		num += add * 4
		add += 2
	return ret

print (spiral_diagonal(1001))

print(time.time() - start)