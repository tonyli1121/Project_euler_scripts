# 50mins
# ----------algorithm--------
#count how many days there will be on that year
#count what the date is when it's Sunday based on above info
# date -= (1+days%7)
# if date==0:
#	date = 7
# elif date == -1:
#	date = 6
# num_of_sundays+=1+(31-date)//7
#--------------------------------
import time

start = time.time()

def isleap(year):
	if year%100 == 0:
		return year%400==0
	else:
		return year%4==0

normalyear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapyear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 1
count = 0

if isleap(1900):
	day+=(sum(leapyear)%7)
else:
	day+=(sum(normalyear)%7)


for year in range(1901,2001):
	for month in range(12):
		if isleap(year):
			day += leapyear[month]%7
		else :
			day += normalyear[month]%7
		if day>7:
			day -= 7
		if day==7:
			count+=1

print (count)
print(time.time()-start)

'''
	days -= date_of_sunday
	date_of_sunday -= (1+days%7)
	
	if date_of_sunday <= 0:
		date_of_sunday += 7

	num_of_sundays += 1+(31-date_of_sunday)//7
	print(date_of_sunday)
	print(num_of_sundays)
错误计算为有多少周日在一月

'''
