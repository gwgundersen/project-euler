'''
DESCRIPTION:
Project Euler, problem 21
Gregory Gundersen, 1/15/2013

PROBLEM:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

SOLUTION:
First, store in a list the sum of the proper divisors of all numbers in the appropriate range.
Then, check if the index and value are amicable. Sum the amicable indices.
'''

import time
import gmath as g
s = time.time()

divs, result = [], 0
for num in range(1,10000):
    divs.append(sum(g.get_proper_divisors(num)))
for i in range(len(divs)):
    if g.is_amicable_pair(i, divs[i-1]):
        result += i

print result

print 'Time: ' + str(time.time() - s)
