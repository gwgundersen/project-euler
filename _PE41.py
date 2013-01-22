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

'''
pandigits = []
for n in range(10000000):
    if g.is_pandigit(list(str(n))):
        pandigits.append(n)
print max(pandigits)'''

def is_pandigit(L, LHash):
    if not L or len(L) == 1:
        return True
    else:
        if L[0] != L[1]:
            if L[0] == n:
                return False
             LHash.append(L[0])
        return is_pandigit(L[1:])

print 'Time: ' + str(time.time() - s)
