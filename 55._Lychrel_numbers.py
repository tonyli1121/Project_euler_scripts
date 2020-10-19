# 10mins
import time

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def rev_and_add(num):
    return num + int(str(num)[::-1])

def is_lychrel(num):
    for i in range(50):
        num = rev_and_add(num)
        if is_palindrome(num):
            return False
    return True

start = time.time()
ans = 0
for num in range(10001):
    if is_lychrel(num):
        ans += 1
        
print(ans)
print(time.time() - start)