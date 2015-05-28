from hashlib import md5

text = "76370c8b218eacfdf6a33bd4c311575a"
boroughs = ["brooklyn", "manhattan", "queens", "bronx", "staten island"]

for first in xrange(0,1000):
    for borough in boroughs:
        for last in xrange(10000, 15000):
            string = "stuyctf{%s_%s_%s}" % (first, borough, last)
            print string
            temp_hash = md5(string)
            if (temp_hash.hexdigest() == text):
                print "The flag is " + string
            else:
                continue
