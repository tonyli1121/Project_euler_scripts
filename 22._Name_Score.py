#29mins

import time

start = time.time()

def sum_of_letters(word):
	return (sum((ord(x) - ord('A') +1) for x in word))

with open ('C:\\Users\\litia\\Desktop\\python\\Archieved Problems\\22._names.txt','r') as f:
	names = f.read()

names = names.replace('\"','').split(',')

names.sort()
ans = 0

for order in range(len(names)):
	ans+=(order+1) * sum_of_letters(names[order])

print(ans)

print(time.time()-start)