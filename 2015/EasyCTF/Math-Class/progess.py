#Both of these versions work locally for me, The latter didnt have time to finish running online.
#I think the problem is that I'm not sure how to accept the input? A file? on the CLI? From a raw_input?
#And idk what to output? A file? just print it out?

'''
Try One:

import sys

given = sys.argv[1:]

answer = 0
if given[0] == 'add':
    answer = abs(int(given[1]) + int(given[2]))
else:
    answer = abs(int(given[1]) - int(given[2]))

print str(answer) + '\n'
'''

#Try 2
given = raw_input('').split(' ')

answer = 0
if given[0] == 'add':
    answer = abs(int(given[1]) + int(given[2]))
else:
    answer = abs(int(given[1]) - int(given[2]))

print str(answer) + '\n'
