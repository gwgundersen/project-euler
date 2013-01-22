'''
 
'''

import time, PE1, PE6

f = open('pe_main_results.txt', 'r+')

s = time.time()
# This should be a lookup table!
if PE1.main() == 233168:
    f.write('PE1: Success!')
    f.write('Time: ' + str(time.time() - s))
    f.write('')
    f.write('Test')

'''
else:
    print 'Failure'
    print

s = time.time()
if PE6.main() == 25164150:
    print 'PE6: Success!'
    print 'Time: ' + str(time.time() - s)
    print
else:
    print 'Failure'
    print

f.write('0123456789abcdef')'''
