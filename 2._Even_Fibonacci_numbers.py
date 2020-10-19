fibonacci_sequence = [1,2,3,5,8,13]
sum = 0

while fibonacci_sequence[-1]<=4000000:
	fibonacci_sequence.append(fibonacci_sequence[-1]+fibonacci_sequence[-2])

for x in fibonacci_sequence:
	if x %2 == 0:
		sum += x

print (sum)
