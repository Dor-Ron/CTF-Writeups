#!/usr/bin/env python

from urllib2 import urlopen

dictionary = urlopen("http://stuyctf.me/problem-static/Trivia-4/dictionary.txt").read()
list_of_words = dictionary.split(" ")

print len(list_of_words)
