import gmath as g

'''
def is_circular_prime(p):
    for i in range(len(str(p))):
        if g.isPrime(p) == False:
            return False
        else:
            sp = str(p)
            for char in sp:
'''

s = '12345'
sl = list(s)

s_first = sl[0]
for i in range(0,len(s)-1):
    sl[i] = sl[i+1]
    print sl
sl[len(s)-1] = s_first

print sl
