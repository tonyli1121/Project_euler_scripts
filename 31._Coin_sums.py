# 50mins
import time

start = time.time()
'''
total = 0
ans = 8

for q in range(2):
     for w in range(4):
          for e in range(10):
               for r in range(20):
                    for t in range(40):
                         for y in range(100):
                              for u in range(200):
                                   if q*100 + w*50 + e*20 + r*10 + t*5 +y*2 +u == 200:
                                        ans += 1
print(ans)
'''
dp = [0 for x in range(201)]
dp[0] = 1
coins = [1, 2, 5, 10, 20, 50, 100, 200]

for c in coins:
	for i in range(c, 201):
		dp[i] += dp[i - c]

print (dp[200])
print(time.time()-start)