"""
Find the millionth lexicographic permutation of the digits 0,1,2,3,4,5,6,8,9
"""
import itertools

digits=[]
for i in range(0,10):
	digits.append(str(i))

count = 1
l = []
for i in itertools.permutations(digits):
	if count == 1000000:
		print i
		break
	count += 1

"""
This one took a lot of foresight.
First difficult question: How do I make all the permutations? 
Do I use strings or ints?
Strings should work, and will probably make it easier in the long run.
Second : How do I put them in order?

Well - then I discovered itertools, and it made everything much much easier.
It can generate permutations in sorted order, and then I just had to break 
the loop at position 1000000.
"""
