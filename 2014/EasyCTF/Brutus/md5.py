from hashlib import md5

#got these from the text files. saves the open().read().split(" ") etc.
numbers = [str(num) for num in xrange(1, 11)] #one-liners == <3
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'black']
animals = ['cats', 'dog', 'mice', 'birds', 'fish', 'turtles', 'elephants', 'snakes', 'pigs', 'cows', 'goats']
adjectives = ['cool', 'smart', 'funny', 'happy', 'weird', 'strange', 'normal', 'big', 'small', 'angry']

string = ""
for idx1 in numbers:
    for idx2 in adjectives:
        for idx3 in colors:
            for idx4 in animals:
                hash = md5(idx1 + idx2 + idx3 + idx4).hexdigest()
                if hash == "f54f10fd6e38929084d505d0c2e9c997":
                    print hash
