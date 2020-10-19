# 70mins

import time

start = time.time()
# generate list of nums in lines
with open('C:\\Users\\litia\\OneDrive\\Archieved Problems\\67._triangle.txt') as f:
    data = f.read()
    
nums = [[int(x) for x in line.split(' ')] for line in data.split('\n')[:-1]]
# to see the result
# print(nums)

# calculate path sum
for row in range(1,len(nums)):
    nums[row][0] += nums[row - 1][0]
    nums[row][-1] += nums[row - 1][-1]
    for column in range(1,len(nums[row])-1):
        nums[row][column]+=max(nums[row-1][column],nums[row-1][column-1])
    
print(max(nums[-1]))

print(time.time() - start)
