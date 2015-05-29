#!/usr/bin/env python

five_hundred_k = int(5 * 10e5)

def fib(n):
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
  return a

param = 0
while True:
    if len(str(fib(param))) == five_hundred_k:
        print str(param) + "\n"
        large_num = fib(param)
        break
    else:
        param += 1

#print large_num
large_num_sum = 0
for num in str(fib(2392483))):
    large_num_sum += int(num)

print large_num_sum #=> 2250347
