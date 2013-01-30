'''
DESCRIPTION:
Project Euler, problem 35
Gregory Gundersen, ../../2013

PROBLEM:
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

SOLUTION:
'''

import time
import gmath as g

def has_no_even_digit(n):
    evens = ['0', '2', '4', '6', '8']
    for e in evens:
        if e in str(n):
            return False
    return True
  
def is_circular_prime(p):
    p_list = list(p)
    p_first = p_list[0]

    for i in range(0,len(str(p))-1):
        p_list[i] = p_list[i+1]

    p_list[len(s)-1] = s_first

    return ''.join(p_list)

def main():

    pg =  g.gen_sieve_of_eratosthenes()
    p = 0
    c = []

    while p < 1000000:
        p = pg.next()
        if has_no_even_digit(p):
            c.append(p)

    return c



s = time.time()
#main()
print 'Time: ' + str(time.time() - s)
