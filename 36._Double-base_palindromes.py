#10mins
import time

def binary(num):
    tmp = str(bin(num))
    return(int(tmp[2:]))

def palindrome(num):
    return str(num) == str(num)[::-1]

start =time.time()

ans = 0

for x in range(1,1000001):
    if palindrome(x):
        if palindrome(binary(x)):
            ans += x
            
print(ans)


print(time.time()-start)