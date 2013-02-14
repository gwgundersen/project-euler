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

def get_reduced_fraction(n, d):

    pg = g.gen_sieve_of_eratosthenes()
    ps = [1]
    if n > d: m = n
    else: m = d

    while ps[len(ps)-1] < m:
        ps.append(pg.next())

    for p in ps:
        if (n % p and d % p) == 0:
            n = int(float(n) / p)
            d = int(float(d) / p)

    print ps
    return [n, d]       


print get_reduced_fraction(8, 4)

'''
cf = []
for n in range(10, 100):
    for d in range(n+1, 100):

        fr = float(n) / d
        n1 = float(str(n)[0])
        n2 = float(str(n)[1])
        d1 = int(str(d)[0])
        d2 = int(str(d)[1])
        
        if (d%10 or d1 or d2) == 0:
            if n1 == d1 and fr == n2 / d2:
                cf.append([n,d])
            if n1 == d2 and fr == n2 / d1:
                cf.append([n,d])
            if n2 == d1 and fr == n1 / d2:
                cf.append([n,d])
            if n2 == d2 and fr == n1 / d1:
                cf.append([n,d])

num, dem = 1, 1
for i in range(len(cf)):
    num *= cf[i][0]
    dem *= cf[i][1]



print cf
print num
print dem
'''
#s = time.time()
#print 'Time: ' + str(time.time() - s)
