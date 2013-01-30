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

# Generate primes
pg = g.gen_sieve_of_eratosthenes()
primes = []
for i in range(200): primes.append(pg.next())
lengths = []

for p in primes:
    length = 1
    tp = p
    i = primes.index(tp)
    print 'PRIME: ' + str(p)
    print 'TEMP: ' + str(tp)
    print 'INDEX: ' + str(i)
    while g.isPrime(tp):
        tp += primes[i+1]
        i += 1
        length += 1
        print 'tp: ' + str(tp)
        print 'i: ' + str(i)
        print 'length: ' + str(length)
    lengths.append(length)
    print

print lengths



 
            
s = time.time()
print 'Time: ' + str(time.time() - s)
