#!/usr/bin/env python

sum1 = 0
for num in xrange(7, args[0]):
    if num % 7 == 0:
        sum1 += num
        
sum2 = 0
for num in str(sum1):
    sum2 += int(num)
    
print sum2
