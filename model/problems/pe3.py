'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

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

def largestPrimeFactor(n, func):
    ans = 0
    i = 0
    maxi = n**0.5
    while i <= maxi:
        if func(i) == True and n % i == 0:
            ans = i
        i += 1
    return ans
            
    

