'''
DESCRIPTION:
Project Euler, problem 41
Gregory Gundersen, ../../2013

PROBLEM:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

SOLUTION:
7652413
'''

import time
import gmath as g

s = time.time()

results = []
for n in range(7654321, 7000000, -2):
    if g.is_pandigital(n) and g.isPrime(n):
        results.append(n)

print max(results)
print 'Time: ' + str(time.time() - s)
