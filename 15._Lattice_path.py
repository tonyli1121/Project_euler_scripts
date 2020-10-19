#27mins
# Lattice path of 20x20

import time
start = time.time()

possiblities = [[y for y in range(21)] for x in range(21)]

def get_possiblities(row,column):
	return(possiblities[row][column - 1] + possiblities[row-1][column])

for row in range(21):
	possiblities[row][0] = 1
for column in range(21):
	possiblities[0][column] = 1


for row in range (1,21):
	for column in range(1,21):
		possiblities[row][column] = get_possiblities(row,column)

print(possiblities[13][13])
print(time.time()-start)