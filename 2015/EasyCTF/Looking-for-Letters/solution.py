import string

info = open("looking-for-letters.in").read()

filtered = [letter for letter in info if letter in string.letters]

file2 = open("looking-for-letters.out", "w")

file2.write("".join(filtered) + '\n')
