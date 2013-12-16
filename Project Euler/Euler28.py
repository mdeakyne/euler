
n = 2
cur = 1
i_sum = 1
for i in range(3,1002,2):
	for j in range(0,4):
		cur = cur + n 
		i_sum = i_sum + cur
	n += 2
print i_sum
		

"""
Spiral diagonals.

Instead of focusing on the image, lets just focus on the pattern

1: 1                    |1 | 1 by 1 spiral
2: 3, 5, 7, 9 :    +2   |24| 3 by 3 spiral
3: 13, 17, 21, 25: +4   |76| 5 by 5 spiral
4: 31, 37, 43, 49: +6   |160|7 by 7 spiral


3,13,31  n+10, n+28
5,17,37  n+12, n+20

Brute force, correct on first try. 
Use range skip to make sure to get all spirals.
Increase n each level, then add four numbers each n higher than the last.

Easy peasy.
"""
