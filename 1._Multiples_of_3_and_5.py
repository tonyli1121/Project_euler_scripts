multiples_of_three_and_five = []
for x in range(1000):
	if not x % 3 or not x % 5:
		multiples_of_three_and_five.append(x)
print(sum(multiples_of_three_and_five))