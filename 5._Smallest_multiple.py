#smallest multiple of 1~20
# 50mins
import time
start = time.time()

n=2520
got_answer = True
while got_answer:
	
    for i in range(20,9,-1):
        if (n %i):
        	break
        if i==10: 
        	print (n)
        	got_answer = False

    n+=2520




'''
num = 2520

while True:
	num+=1
	count = 0
	for x in range(2,21):
		if not num%x:
			count+=1
		else:
			break
	if count == 19:
		print (num)
		break
	elif count<19:
		continue
	else:
		print('ERROR')
'''
end = time.time()
print(end - start)


