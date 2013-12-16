"""
1. find proper divisors of a number
2. determine if a number is "abundant" (proper divisors added together)
3. sum all abundant numbers which add up to less than 28123
4. iterate through ignoring those numbers and sum

Any integers greater than 28123 can be written as the sum of two abundant numbers
"""
#proper divisors of a number
#determinig if number is abundant
def is_abundant(n):
	#avoid adding n as a divisor, but keep 1.
	divisors = [1] 
	#start at 2 and go until sqrt(n) cuts down iterations
	for i in range(2,int(n**.5)+1):
		if n%i==0:
			divisors.append(i)
			if not n/i == i:
				divisors.append(n/i)
	return sum(divisors) > n
	
abundant_nums = [] 
sum_two_abundant =[]

#this is a brute force approach, and could probably be more elegant
#however it does work in about 3 seconds.
for n in range(2,28124):
	if is_abundant(n):
		sum_two_abundant.append(n+n)
		for i in abundant_nums:
			if(n+i <= 28123):
				sum_two_abundant.append(n+i)
		abundant_nums.append(n)

#print abundant_nums[0]
#print sum_two_abundant[0]
set_abundant_sums = set(sum_two_abundant)

count_non_abundant = 0
for i in range(1,28124):
	if i not in set_abundant_sums:
		count_non_abundant += i

print count_non_abundant
		
"""
Notes on mistakes made:
1. 4 showed up as being abundant, due to adding n and n/i.
Had to add a check to make sure n/i wasn't equal to i (line 18, 19)
2. 24 was not the lowest number in sum_two_abundant. 
I wasn't appending n+n, so it was only adding two distinct abundant
numbers. Had to add this in. (line 27)
3. Having trouble with upper limit.
Made all ranges include 28123, but then changed line 29 to be <= and
that fixed it. Apparently 28123 can be expressed at the sum of two 
abundant numbers and wasn't being added in, so my answer was off by that 
much.
""" 

