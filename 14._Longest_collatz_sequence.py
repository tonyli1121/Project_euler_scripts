# <5mins 暴力求解 方法正确可是出不来答案

import time
start = time.time()

sequence = {}

def terms_of_sequence(startvalue):
	_terms = 1
	tmp = startvalue
	while not tmp == 1:
		if tmp in sequence.keys():
			_terms += sequence[tmp]
			break
			#!!!!!!!!这里：如果出现之前计算中出现的数，直接加上去
		_terms+=1

		if tmp%2==0:
			tmp = tmp/2
		elif tmp%2:
			tmp = tmp*3 -1
	sequence[startvalue] = _terms
	return _terms

terms = 0
ans = 0
for n in range(1000000):
	if terms_of_sequence(n)>terms:
		terms = terms_of_sequence(n)
		ans = n

print (ans)

print(time.time() - start)