#!/usr/bin/python

count = 0

price = 1827.43

while(price > .01):
    if price >= 0.25:
        price -= .25
    elif price >= 0.1 and price < .25:
        price -= .10
    else:
        price -= .01
    count += 1
    # For debugging
    print "The price is:\t" + str(price)
    print "Coin count:\t" + str(count) + '\n'

#print count # ==> 7318
