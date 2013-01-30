'''
DESCRIPTION:
Project Euler, problem 47
Gregory Gundersen, ../../2013

PROBLEM:
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?


SOLUTION:
296962999629
'''

import time
import gmath as g
           
def main():
    
    pg =  g.gen_sieve_of_eratosthenes()
    p, primes = 1, []
        
    while p < 10000:
        p = pg.next()
        p2 = p + 3330
        p3 = p + 6660
        if g.isPrime(p2) and g.isPrime(p3):
            if g.is_permutation(p, p2) and g.is_permutation(p, p3):
                primes.append([str(p), str(p2), str(p3)])

    return ''.join(primes[1])

s = time.time()
print main()
print 'Time: ' + str(time.time() - s)
