"""----------------------------------------------------------------------------
Project Euler
Gregory Gundersen
2013-01

Problem:
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99. Find the largest
palindrome made from the product of two 3-digit numbers.

Solution:
Brute-force. The computational expense is primarily with the nested for loops.
We can reduce this search space?
----------------------------------------------------------------------------"""


import gmath


def main():
    result = 0
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            if gmath.is_palindromic_number(i*j):
                temp = i*j
                if temp > result:
                    result = temp
    return result
