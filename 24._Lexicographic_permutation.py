# 86 mins
import time

digits = ['0','1','2','3','4','5','6','7','8','9']

def lexicographic_permutation(n):
	count = 0
	for a in digits:
		number = ''
		number += a
		tmp1 = number
		#print(tmp1)
		#------
		for b in digits:
			if b == a:
				continue
			number = tmp1
			number += b
			tmp2 = number
			#print(tmp2)
			#---------
			for c in digits:
				if c == a or c == b:
					continue
				number = tmp2
				number += c
				tmp3 = number
				#print(tmp3)
				#---------------
				for d in digits:
					if d == a or d == b or d == c:
						continue
					number = tmp3
					number += d
					tmp4 = number
					#print(tmp4)
					#------------
					for e in digits:
						if e == a or e == b or e == c or e == d:
							continue
						number = tmp4
						number += e
						tmp5 = number
						#print(tmp5)
						#-----------
						for f in digits:
							if f == a or f == b or f == c or f == d or f == e:
								continue
							number = tmp5
							number += f
							tmp6 = number
							#print(tmp6)
							#----------
							for g in digits:
								if g == a or g == b or g == c or g == d or g == e or g == f:
									continue
								number = tmp6
								number += g
								tmp7 = number
								#print(tmp7)
								#--------------
								for h in digits:
									if h == a or h == b or h == c or h == d or h == e or h == f or h == g:
										continue
									number = tmp7
									number += h
									tmp8 = number
									#print (tmp8)
									#----------
									for i in digits:
										if i == a or i == b or i == c or i == d or i == e or i == f or i == g or i == h:
											continue
										number = tmp8
										number += i
										#tmp9 = number
										#print (tmp9)
										#-------------
										for j in digits:
											if j == a or j == b or j == c or j == d or j == e or j == f or j == g or j == h or j == i:
												continue
											number += j
											count += 1 
											#print(f'{count} {number}')
											if count == n:
												return number
											
start = time.time()

print(lexicographic_permutation(1000000))
print(time.time()-start)