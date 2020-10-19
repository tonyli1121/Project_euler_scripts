# 15 mins
import time

def list_of_multiples(num):
    return [str(num*x) for x in range(1,7)]

def permuted(nums):
    for x in range(1,6):
        if sorted(nums[x]) != sorted(nums[0]):
            return False
    return True

start = time.time()
ans = 1
while True:
    if permuted(list_of_multiples(ans)):
        print(ans)
        break
    ans += 1
    
print(time.time()-start)