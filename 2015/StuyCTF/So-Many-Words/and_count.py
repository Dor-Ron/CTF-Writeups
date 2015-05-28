#!/usr/bin/env python

from urllib2 import urlopen

words = urlopen("http://stuyctf.me/problem-static/So-Many-Words/dictionary.txt").read()
list_of_words = words.split("\n")

count = 0
for word in list_of_words:
    if "and" in word:
        count += len(word)
    else:
        continue

print "stuyctf{%d}" % count #=> stuyctf{38441}
