'''
DESCRIPTION:
Project Euler, problem 33
Gregory Gundersen, ../../2013

PROBLEM:
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it
may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

SOLUTION:
'''

import time
import gmath as g

def is_common_divisor(n1, n2, d):
    if d==0:
        return False
    if n1%d == 0 and n2%d == 0:
        return True
    return False

cf = []
for n in range(1, 100):
    for d in range(n+1, 100):
        for i in range(n):
            if is_common_divisor(n, d, i) == False:
                cf.append([n, d])

print cf

'''
        n1 = float(str(n)[0])
        n2 = float(str(n)[0])
        d1 = int(str(d)[0])
        d2 = int(str(d)[0])
        
        fr = float(n) / d

        if n/10==n1 and d/10 == d1:
            break

        if fr==n1/n1
            cf.append(n1/d1)
        if fr==n1/d2:
            cf.append(n1/d2)
        if fr==n2/d1:
            cf.append(n2/d1)
        if fr==n2/d2:
            cf.append(n2/d2)

print cf

#s = time.time()
#print 'Time: ' + str(time.time() - s)'''
