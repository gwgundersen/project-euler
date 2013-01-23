'''
DESCRIPTION:
Project Euler, problem 41
Gregory Gundersen, ../../2013

PROBLEM:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

SOLUTION:
'''

import time
import gmath as g

s = time.time()

def get_primes_in_range(lo, hi):
    if lo % 2 == 0:
        lo -= 1
    while g.isPrime(lo) == False:
        lo -= 2
    primes = []
    primes.append(lo)
    for n in range(lo, hi+1, 2):
        if g.isPrime(n):
            primes.append(n)
    return primes

def sieve(lo, hi):
    if lo % 2 == 0:
        lo -= 1
    if g.isPrime(lo) == False:
        while g.isPrime(lo) == False:
            lo -= 1

	nums = range(lo, hi+1, 2)

	for n in nums:
		m = 2
		while n * m <= nums[-1]:
			if n * m in nums:
				nums.remove(n*m)
			m += 1
	return nums

print sieve(50,100)

print 'Time: ' + str(time.time() - s)
