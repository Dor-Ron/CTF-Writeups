recv = open("math-class.in").read().split(" ")

solution = 0
if recv[0] == "add":
	solution = abs(int(recv[1]) + int(recv[2]))
elif recv[0] == "subtract":
  	solution = abs(int(recv[1]) - int(recv[2]))


file2 = open("math-class.out", "w").write(str(solution) + '\n')
