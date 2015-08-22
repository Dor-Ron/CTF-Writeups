# Bandit Level 7 → Level 8
===========================

**problem**

The password for the next level is stored in the file data.txt next to the word *millionth*

**Solution**

Pretty simple, first `ls` to see if *data.txt* is in the directory, it is, let's continue.
We can just use `grep` to return all the contents of the line where a specific word is located.

`grep "millionth" data.txt`

Gives back:

`millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV`

Flag: **cvX2JJa4CFALtqS87jk27qwqGhBM9plV**
