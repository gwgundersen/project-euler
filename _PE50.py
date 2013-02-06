'''
DESCRIPTION:
Project Euler, problem 50
Gregory Gundersen, ../../2013

PROBLEM:
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

SOLUTION:
'''

import time
import gmath as g

s = time.time()

# Generate primes
pg = g.gen_sieve_of_eratosthenes()
primes = []
lim = 1000000
while True:
    p = pg.next()
    if p < lim:
        primes.append(p)
    else:
        break

lens = []
for i in range(0, len(primes)):
    
    for j in range(1, len(primes), 2):

        # uncomment the line below if the two loops are confusing
        # print primes[j:len(primes)-i]

        sm = sum(primes[j:len(primes)-i]) # the sum of the primes
        ln = len(primes[j:len(primes)-i]) # the len of the primes

        if g.isPrime(sm) and sm < lim:
            lens.append(ln)



        # uncomment the line below if the two loops are confusing
        # print primes[j:len(primes)-i]

        #sm = sum(primes[j:len(primes)-i]) # the sum of the primes
        #ln = len(primes[j:len(primes)-i]) # the len of the primes

        #if g.isPrime(sm) and sm < lim:
        #    lens.append(ln)

print max(lens)

print 'Time: ' + str(time.time() - s)
