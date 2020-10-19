# 08 - 59 give up for now
'''
#High Card: Highest value card.
#One Pair: 2
#Two Pairs: Two different pairs. (3)
#Three of a Kind: Three cards of the same value. 4
#Straight: All cards are consecutive values. 5
#Flush: All cards of the same suit. 6
#Full House: Three of a kind and a pair. 7
#Four of a Kind: Four cards of the same value. 8
#Straight Flush: All cards are consecutive values of same suit. 9 
#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. 10
'''

import time


player1 = []
player2 = []

with open('C:\\Users\\litia\\Desktop\\python\\Archieved Problems\\54._poker.txt') as f:
    plays = f.read().split('\n')

#print(plays)

for hands in plays:
    player1.append(hands[0:14].split(' '))
    player2.append(hands[15:29].split(' '))

print(player1)
print(player2)