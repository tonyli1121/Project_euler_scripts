'''
n ===> num of digits

10^(n-1)<=N<=n*362880

10^(n-1) - 362880n <=0

n<8

'''
# 20mins got ans  40mins better solution
import time

def factorial(num):
    total = 1
    for x in range(1,num+1):
        total *= x
    return total

def digit_factorials(num):
    tmp = str(num)
    sums = 0
    for digit in tmp:
        sums += facto[digit]
    return sums == num
    
start = time.time()

facto = {'0':1}

for x in range(1,10):
    facto[str(x)] = factorial(x)

ans = 0


for x in range(3,100000):
    if digit_factorials(x):
        ans+=x

print(ans)
print(time.time() - start)