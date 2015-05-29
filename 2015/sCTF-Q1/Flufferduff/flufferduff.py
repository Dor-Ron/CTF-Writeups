#!/usr/bin/env python

from math import sqrt

'''
Instructions

Let *(n) = d(n) - x(n) where x(n) is the sum of all odd numbers above 0 and before n, exclusive, and d(n) is the sum of all primes in the range of (0,n), exclusive.

When *(n) is negative, we call this a flufferduff.

Find the number of flufferduffs below 1000.
'''

def prime_test(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
 
#print prime_test(7)

prime_array = []
for num in range(1000):
    if prime_test(num):
        prime_array.append(num)

odd_array = range(1, 1000, 2)

def prime_total(n):
    if n in prime_array:
        return sum(prime_array[:prime_array.index(n)])
    else:
        for num in xrange(n, 1, -1):
            if num in prime_array:
                return sum(prime_array[:prime_array.index(num)])
            else:
                continue
            
def odd_sum(n):
    if n in odd_array:
        return sum(odd_array[:odd_array.index(n)])
    else:
        return sum(odd_array[:odd_array.index(n-1)])

fluffer_count = 0
for num in xrange(1, 1000):
    if prime_total(num) - odd_sum(num) < 0:
        fluffer_count += 1

print fluffer_count 
