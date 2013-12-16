from decimal import *


l_candidates = []
getcontext().prec=2000
for i in range(2,1000):
	d = Decimal(1) / Decimal(i)
	s = str(d)
	s = s[4:]
	if len(s) > 1000:
		front = ""
		for j in range(0,len(s)):
			front += s[j]
			if front == s[j+1:j+len(front)+1]:
				if(len(front)>900):
					l_candidates.append((i,len(front)))
				break
			
print l_candidates

	
"""
Had a hard time figuring out how to cut off the number past the decimal point
String limits the represenations to 12 decimal points
Had to use string formatting to better represent the numbers.


What if, instead of using strings and floats, I do the math myself?
No.

Using decimal helps. 
Narrow down based on length of the repeating numbers.
Further narrowed down based on length of individual numbers.

Still have 465 candidates after using these filters. Not helpful.

down to 81 candidates after using decimal.

Ok, wrong answer : 97, which has 96 repeating decimal.
-Learned to increase precision.
-Taking a string and building it slowly. comparing to see if it repeats.

Another wrong anser: 998, which has 498 repeating. I got this by cutting off the first number.
Used a decimal point precision of 1000. Increasing to 5000.

With 5000 : 983 gives us 982 repeating points. So 2000 approximation should work. 
Wrong again. This is frustrating. 

With 10000, I'm still getting 983 with 982 repeating cycle. It takes awhile here.
Even changing to allow for the repetition to start later, still getting same answer.

AAAARRGGG: I tried 982 in the answer spot previously. It is actually 983. 
Well verified. Condensed it to include the string check in the first run through. 
No use building a list of things we will ignore eventually.
2000 

1. Miss it if you don't account for the first number not being in the cycle.
2. Need accuracy to at least 2000 places
"""
