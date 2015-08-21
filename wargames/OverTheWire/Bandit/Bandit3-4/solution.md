We ssh into bandit3. Once we gain access to the remote server, we run the `ls` command,
as we're told we need to look for the *inhere* directory, we find it and `cd` into it with
`cd inhere`. Once in *inhere* we run `ls` again, but don't see anything. I approached the problem
in 2 ways.

1) `ls -a` the -a flag shows us all files and directories. even hidden ones.

2) `find .` period being and branch off the pwd

Both approaches lead to a file name called **.hidden**

We run `cat .hidden` and find the flag.

Flag **pIwrPrtPN36QITSp3EQaw936yaFoFgAB**
