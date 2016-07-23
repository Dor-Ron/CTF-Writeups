# Solution, GZ, 30
---

We're given a file, `cd` into the directory where you downloaded it. run

`file flag` where flag is the name of the file you downloaded.

It tells us:


    flag: gzip compressed data, was "flag", from Unix, last modified: Sun Jun 26 13:22:38 2016

So we use the `gzip` command to decompress the file

`gzip -cd flag > flag2`

Just read flag2 with `cat` to get the final flag, which is:

Flag: **ABCTF{broken_zipper}**
