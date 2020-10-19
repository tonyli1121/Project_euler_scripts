#40mins
import time

num_in_order = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def check_pandigital(mult1,mult2,product):
    tmp = str(mult1) + str(mult2) + str(product)
    tmp = sorted(tmp)
    if tmp == num_in_order:
        return True
    return False

start = time.time()

pandigital = set()
# x and y cannot be 2(or 3)-digits respectively at the same time

ans = 0
for x in range(2,10000):
    # 4 digits ====== 1 digit
    if x >=1000:
        for y in range(2,10):
            product = 1
            product = x*y
            if check_pandigital(x,y,product):
                pandigital.add(product)
    # 3 digits ====== 2 digits
    elif x>=100:
        for y in range(10,100):
            product = 1
            product = x*y
            if check_pandigital(x,y,product):
                pandigital.add(product)    
    # 2 digits ====== 3 digits
    else:
        for y in range(100,1000):
            product = 1
            product = x*y
            if check_pandigital(x,y,product):
                pandigital.add(product)

print(sum(pandigital))
print(time.time()-start)