A google search for finding only human readable files didn't really work...
Knowing that I'd need to use the `file` command I read the docs for it using `man file`
The examples show using `file -s <path>` on a list of files, which would save me the trouble of looking at
each file iindividually. So after a quick `cd` into the directory and `ls` I noticed that all the filenames 
had a lot in common. I ran `pwd` to get the path flag for the `file` command. And ran the following:

`file -s /home/bandit4/inhere/-file0{0,1,2,3,4,5,6,7,8,9}`

Which gave me the following output:

    /home/bandit4/inhere/-file00: data
    /home/bandit4/inhere/-file01: data
    /home/bandit4/inhere/-file02: data
    /home/bandit4/inhere/-file03: data
    /home/bandit4/inhere/-file04: data
    /home/bandit4/inhere/-file05: data
    /home/bandit4/inhere/-file06: data
    /home/bandit4/inhere/-file07: ASCII text
    /home/bandit4/inhere/-file08: data
    /home/bandit4/inhere/-file09: data

The salient file being **./-file07** So I ran:

`cat ./-file07`

And got the flag.

Flag: **koReBOKuIDDepwhWk7jZC0RTdopnAYKh**

