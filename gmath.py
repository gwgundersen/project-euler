'''
The following is a library of useful mathematical functions for Project Euler
Most of the scripts were written by Gregory Gundersen, although some of them are not original
The library has been compiled by Gregory Gundersen
'''

def isOdd(n):
    if n % 2 == 0:
        return False
    else:
        return True

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

def getPrimeFactors(n):
    primeFactors = []
    for p in genPrimes(10):
        if p*p > n:
            break
        while n % p == 0:
            primeFactors.append(p)
            n //= p
    if n > 1:
        primeFactors.append(n)

    return primeFactors

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
    divs = []
    for num in range(1,n):
        if n % num == 0:
            divs.append(num)
    return divs

def is_amicable_pair(a,b):
    if sum(get_proper_divisors(a)) == b and sum(get_proper_divisors(b)) == a and a != b:
        return True
    else:
        return False
