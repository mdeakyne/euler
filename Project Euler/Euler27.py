import primes

l_numprimes=[]
for a in range(-1000,1000):
	print a
	for b in range(-1000,1000):
		n = 0
		while(True):
			if(primes.isprime(n**2+a*n+b)):
				n+=1
			else:
				l_numprimes.append((n,a,b))
				break
l_numprimes.sort(reverse=True)
print l_numprimes[0]

"""
First time through, brute force approach.
Go from -1000 to 1000 in a and b.
Check n while it's prime.

Spun for awhile, printing a each time.

Oh - had an infinite while loop. Added a break to the else.
Much faster :)

Changed sort to reverse = True.
Got 71 consecutive primes, which is less than the 80 consecutive primes 
from -79 and 1601. 

Let's try it, I guess. (oh 1601 > 1000). Correct!

"""
