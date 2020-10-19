#41mins


import time

hundredth = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
tenth = {9:'ninety',8:'eighty',7:'seventy',6:'sixty',5:'fifty',4:'forty',3:'thirty',2:'twenty'}
special = {0:'ten',1:'eleven',2:'twelve',3:'thirteen',4:'fourteen',5:'fifteen',6:'sixteen',7:'seventeen',8:'eighteen',9:'nineteen'}
oneth = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

def len_of_numstr(num):

	tmp = num
	text = ''
	if num == 1000:
		text+='onethousand'
		tmp %= 1000
	while tmp != 0:	
		#hundredth digit word length count & 'and' if there's number after moduling 100
		if tmp//100:
			text += hundredth[tmp//100] + 'hundred'
			if tmp%100:
				text += 'and'
			tmp %= 100

		elif tmp//10:
			# ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
			if tmp//10 == 1:
				text += (special[tmp%10])
				break
			else:
				text += (tenth[tmp//10])
			tmp %= 10

		elif tmp//1:
			text += (oneth[tmp//1])
			tmp %= 1

	return(len(text))



start = time.time()

total_length = 0

for num in range(1, 1001):
	total_length+=len_of_numstr(num)

print(total_length)
print(time.time() - start)