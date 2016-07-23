f = open("addition.in").read().strip('\n').split(",")
d = sum([int(q) for q in f])

x = open("addition.out", "w")
x.write(str(d) + '\n')
