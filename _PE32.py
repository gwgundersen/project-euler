'''
DESCRIPTION:
Project Euler, problem 32
Gregory Gundersen, ../../2013

PROBLEM:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 * 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

SOLUTION:
Lo: 1 * 1000 = 1000
Hi: 1 * 999 = 9999 
'''

import time
import gmath as g

def main():
    result = 0
    for x in range(1, 99):
        for y in range(1, 9999):
            z = str(x) + str(y) + str(x*y)
            if g.is_pandigital(z) and len(z) == 9: #and len(str(x)) < 3:
                print str(x) + ' * ' + str(y) + ' = ' + str(x*y) + ': ' + str(z)
                result += (x*y)
    return result
            
s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
