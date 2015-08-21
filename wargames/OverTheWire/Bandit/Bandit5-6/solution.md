This one wasn't as difficult as I thought it'd be, as I found only one
matching file without having to check all the criteria.

I `cd` into **inhere**, and then `find .`.

Saw there was a bunch of possiblities so I began attempting to narrow them down.


`find . -type f -size 1033c`

This search assured human readablity and proper size. Luckily only one file was printed to the screen

`./maybehere07/.file2`

Now that I found the correct file. simply `cd maybehere07 && cat ./.file2`

Flag: **DXjZPULLxYr17uwoI01bNLQbtFemEgo7**
