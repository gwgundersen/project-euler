'''
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random,
it can be seen that the probability of taking two blue discs, P(BB) = (15/21)*(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,
is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total,
determine the number of blue discs that the box would contain.
'''

import time
s = time.time()

def boxProb(box):
    return round(
        (box['b']/float(box['b']+box['r'])) * \
        ((box['b']-1)/float(box['b']+box['r']-1)) \
        , 10
        )

def boxSize(box):
    return box['b']+box['r']

# MAIN PROGRAM
m = 1000
for r in range(1, m):
    for b in range(2*r, 3*r):
        if boxProb({'b':b, 'r': r}) == 0.5 and boxSize({'b':b, 'r': r}) > 1:
            print {'b':b, 'r': r}

print 'Time: ' + str(time.time() - s)





