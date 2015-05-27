#!usr/bin/env python
# -*- coding: utf-8 -*-
#make sure you're .py file is in the same directory as your pictures

from hashlib import md5
from PIL import Image

#part one
'''
images = []
#making array of image names
for i in xrange(10):
    images.append("pixels" + str(i) + ".png")
r_sum = 0
g_sum = 0
b_sum = 0
for j in xrange(300):
    for k in xrange(300):
        img = Image.open(images[9]) #change index when you run code
        rgb_im = img.convert('RGB')
        r, g, b = rgb_im.getpixel((j, k))
        r_sum += r
        g_sum += g
        b_sum += b
print r_sum, g_sum, b_sum
'''

#Results for each picture based off commented out code above
d={}
d['img0'] = {"r": 11494362, "g": 11456512, "b": 11455046}
d['img1'] = {"r": 11465267, "g": 11526812, "b": 11458528}
d['img2'] = {"r": 11497420, "g": 11503629, "b": 11460281}
d['img3'] = {"r": 11477885, "g": 11492201, "b": 11463703}
d['img4'] = {"r": 11465260, "g": 11486146, "b": 11469840}
d['img5'] = {"r": 11479362, "g": 11467199, "b": 11456036}
d['img6'] = {"r": 11488624, "g": 11475854, "b": 11496154}
d['img7'] = {"r": 11456042, "g": 11438366, "b": 11469108}
d['img8'] = {"r": 11468025, "g": 11499165, "b": 11490386}
d['img9'] = {"r": 11475589, "g": 11463840, "b": 11440649}

final=""

for x in sorted(d.keys()):
    final+=md5(md5(str(d[x]['r'])).hexdigest() + md5(str(d[x]['g'])).hexdigest() + md5(str(d[x]['b'])).hexdigest()).hexdigest()

print md5(final).hexdigest()
