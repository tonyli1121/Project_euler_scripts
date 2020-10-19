# 30mins

import time

def palin_products(num):
    tmp = str(num)
    return (''.join(sorted(tmp))) == '123456789'


start = time.time()

ans = 0

for x in range(1,10000):
    product = ''
    for y in range(1,10):
        if len(product)>=9:
            break            
        product += str(x*y)
    if palin_products(product):
        ans = max(int(product),ans)
    

print(ans)

print(time.time() - start)