# largest
# palindrome product of 3-digits
# 40mins
import time
start = time.time()

palindrome = 1
for i in range(999,99,-1):
	for j in range(999,i-1,-1):
		product = i*j
		if str(product) == str(product)[::-1] and product > palindrome:
			palindrome = product
			break
print (palindrome)

end = time.time()
print (end-start)

