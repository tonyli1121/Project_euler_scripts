#24mins

import time
from math import sqrt
def word_score(word):
    tmp = 0
    for letter in word:
        tmp += ord(letter) - ord('A')+1
    return tmp

def triangular_num(num):
    tmp = 2*num
    return tmp == (int(sqrt(tmp))+1)*(int(sqrt(tmp)))

start = time.time()

with open('C:\\Users\\litia\\Desktop\\python\\Archieved Problems\\42._words.txt','r') as f:
    words = f.read()
    
words = words.replace('\"','').split(',')

count = 0

for word in words:
    if triangular_num(word_score(word)):
        count+=1

print(count)

print(time.time() - start)