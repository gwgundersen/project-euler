'''
DESCRIPTION:
Project Euler, problem 31
Gregory Gundersen, 1/../2013

PROBLEM:
In England the currency is made up of pound, L, and pence, p,
and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).

It is possible to make L2 in the following way:
1*L1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can L2 be made using any number of coins?

SOLUTION:
'''

import time
s = time.time()

coins = [100, 50, 20, 10, 5, 2, 1]
mark = 200

1+1+1+...+1+1+1 = 200
1+1+1+...+1+2   = 200




def get_change(coins, mark):





print 'Time: ' + str(time.time() - s)
