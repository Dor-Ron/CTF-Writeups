poem = open('poem.txt').read().split(" ")
flag = ""
for word in range(len(poem)):
    if word % 3 == 2:
        flag += poem[word]
punctuation = '?".,\'!`;:'
for sign in punctuation:
    flag = flag.replace(sign, '')

solution = "stuyctf{" + flag + "}"
print solution.replace("\n", "")
