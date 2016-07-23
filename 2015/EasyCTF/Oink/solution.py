file1 = open('piglatin1.in').read().strip('\n').split(" ")

lst = []
for word in file1:
  if word[0] in 'aeiouAEIOU':
    lst.append(word + 'yay')
  else:
    lst.append(word[1:] + word[0] + 'ay')

file2 = open('piglatin1.out', 'w').write(" ".join(lst) + '\n')
