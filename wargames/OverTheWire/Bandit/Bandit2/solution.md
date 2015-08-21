Still on the bandit1 host, we run `ls` and get this returned **-**,
Which is expected because we are told the password is hidden in that file.
I naively tried running `cat -` but bash didn't react accordingly.
I then though "You can't outsmart me," knowing that most linux machines are preinstalled with python.
I ran `python` and typed `open('-').read()` in the REPL, which should be pretty self explanatory.
And got the password for Level 2. But I knew that's not what the problem was supposed to teach me, and
googled the suggested "dashed filename." I found the following Unix Stack Exchange [thread](http://unix.stackexchange.com/questions/16357/usage-of-dash-in-place-of-a-filename) 
and noticed the following: **The usual way of doing this is to prefix the filename with a path -** `./-`.
So I ran `cat ./-` and sure enough I was shown the password.


Password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
