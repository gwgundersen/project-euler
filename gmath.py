'''
The following is a library of useful mathematical functions for Project Euler
Most of the scripts were written by Gregory Gundersen, although some of them are not original
The library has been compiled by Gregory Gundersen
'''
import time

def isOdd(n):
    if n % 2 == 1:
        return True
    return False

def isPrime(n):
    if n < 0:
        raise ValueError
    elif isinstance(n, int) == False:
        raise TypeError
    else:
        maxi = n**0.5
        i = 3
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        else:
            while i <= maxi:
                if n % i == 0:
                    return False
                i += 2
            return True

def genPrimes():
    primes, n, i = [2], 1, 1
    yield 2
    while True:
        n += 1
        for p in primes:
            if (n % p) == 0:
                break
        else:
            primes.append(n)
            yield n

def gen_primes_from_p(p):
    primes, n, i = [2], 1, 1
    yield p
    while True:
        n += 1
        for p in primes:
            if (n % p) == 0:
                break
        else:
            primes.append(n)
            yield n


def sieve_of_atkin(limit):

    # initialize
    primes = [2,3,5]
    sieve = [False]*(limit+1)
    sqrt_limit = int(limit**0.5)

    # generate primes
    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4*x**2+y**2
            if (n <= limit) and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if (n <= limit) and (n % 12 == 7):
                sieve[n] = not sieve[n]
            n = 3*x**2-y**2
            if x > y and (n <= limit) and n % 12 == 11:
                sieve[n] = not sieve[n]

    # eliminate composites
    for i in range(5, sqrt_limit):
        if sieve[i]:
            for j in range(i**2, limit, i**2):
                sieve[j] = False

    # finalize
    for i in range(7, limit):
        if sieve[i]:
            primes.append(i)
    return primes

def get_prime_factors(n):
    primeFactors = []
    for p in genPrimes():
        if p*p > n:
            break
        while n % p == 0:
            primeFactors.append(p)
            n //= p
    if n > 1:
        primeFactors.append(n)

    return primeFactors

def gen_triangle_number():
    tri, inc = 1, 1
    yield 1
    while True:
        inc += 1
        tri += inc
        yield tri

def genComposites():
    yield 4
    n = 5
    while True:
        if not isPrime(n):
            yield n
            n += 1
        else:
            n += 1

def genCompositesOdd():
    yield 9
    n = 15
    while True:
        if not isPrime(n) and isOdd(n):
            yield n
            n += 2
        else:
            n += 2

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def getFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return getFibonacci(n-1) + getFibonacci(n-2)

def genFibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def getFigurate(n, M):
    return (factorial(M+n-1) / factorial(M-1)) / factorial(n)

def get_proper_divisors(n):
    divs = [1]
    for num in range(2, n/2+1):
        if n % num == 0:
            divs.append(num)
    return divs

def is_amicable_pair(a,b):
    if sum(get_proper_divisors(a)) == b and sum(get_proper_divisors(b)) == a and a != b:
        return True
    return False

def is_perfect(n):
    if sum(get_proper_divisors(n)) == n:
        return True
    return False

def is_abundant(n):
    if sum(get_proper_divisors(n)) > n:
        return True
    return False

def is_deficient(n):
    if sum(get_proper_divisors(n)) < n:
        return True
    return False

def is_palindrome(n):
    sn = str(n)
    if len(sn) == 1 or (len(sn) == 2 and sn[0] == sn[1]):
        return True
    else:
        L = len(sn)-1
        if sn[0] == sn[L]:
            sn = sn[1:L]
            return is_palindrome(sn)
        else:
            return False

def base10_to_baseK(n, K, L):
    # L is an empty list
    if n == 0:
        L.reverse()
        b = map(str, L)
        b = ''.join(b)
        return int(b)
    else:
        L.append(n % K)
        return base10_to_baseK(n/K, K, L)

def get_alphabet_value_char(char):
    alphabet_values = {
        'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
        'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
        }
    return alphabet_values[char.lower()]

def get_alphabet_value_word(word):
    value = 0
    for char in word:
        value += get_alphabet_value_char(char)
    return value

def is_pandigital(n):
    L = map(str, range(1, len(str(n))+1))
    for d in str(n):
        if d in L:
            L.remove(d)
        else:
            return False
    return True

def concatenated_product(n, L):
    s = ''
    for num in L:
        s += str(num * n)
    return int(s)

def is_truncatable(n):
    s = str(n)
    l = len(s)
    if l < 2 or not isPrime(n):
        return False
    for x in range(l):
        if not isPrime(int(s[x:])):
            return False
    for x in range(l, 0, -1):
        if not isPrime(int(s[:x])):
            return False
    return True

def is_pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    return False
