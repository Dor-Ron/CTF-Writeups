x = open("can-you-even.in").read().strip("\n").split(",")

f = str(len(list(filter(lambda w: int(w) % 2 == 0, x))))

j = open("can-you-even.out", "w")
j.write(f + '\n')
