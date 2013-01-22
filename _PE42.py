'''
DESCRIPTION:
Project Euler, problem 42
Gregory Gundersen, ../../2013

PROBLEM:

SOLUTION:
'''

import time

s = time.time()

result = 0

'''
PSEUDO CODE:
For each word in words.txt, generate alphabetical value
Compare to hash table of triangle numbers
Add up triangle words
'''


# process file
f = open('pe42_words.txt','r')
wordList = f.read().split(',')
wordList = [word.strip for word in wordList
f.close()

print wordList

# each word in words.txt is split by " symbol

print 'Time: ' + str(time.time() - s)
