# if (a+b+c=1000) and  (a**2 + b**2 == c**2): print(a*b*c)
# 28mins

import time

start = time.time()

a = 0
b = 0

for x in range(3,334):
	for y in range(x+1,(1000-x)//2):
		c = 1000-(x+y)
		if ((x**2)+(y**2)==(c**2)):
			a = x
			b = y
			break
	if ((a**2)+(b**2)==(c**2)):
		break

print(a*b*c)

end = time.time()
print(end - start)