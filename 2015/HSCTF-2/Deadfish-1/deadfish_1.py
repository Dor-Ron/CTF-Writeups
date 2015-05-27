#!/usr/bin/env python

# Initialization
accumulator = 0

string = "iiisdddsddddddddddddddddsdddd"
if accumulator == 256 or accumulator == -1:
    # Overflow, reset accumulator
    accumulator = 0
# Process input
for letter in string:
    if letter == "i":
        accumulator += 1
    elif letter == "d":
        accumulator -= 1
    elif letter == "s":
        accumulator *= accumulator
    elif letter == "o":
        print accumulator
    else:
        print "Unrecognized command"

print accumulator #=> 396
