# 17-18 && 18-19

This is really part of a 2 part problem, but to get the password for bandit 18, we need to run:

`diff passwords.new passwords.old`

this returns:

    42c42
    < kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
    ---
    > PRjrhDcANrVM6em57fPnFp4Tcq8gvwzK

The change we want is the top one, since we passed the **.new** file first.

So we try: `ssh bandit18@localhost` but we get back:

    Byebye!
    Connection localhost closed.

Because someone altered the **.bashrc** to automatically log us out when we log in. So we need execute `cat readme` in conjunction with out `ssh` command. To see the password for the next level.

We accomplish that by `ssh -t bandit18@localhost /bin/sh`

This will allow us to run unlimited amount of bash prompts logged in as bandit18.

We're prompted `>` and we just enter `cat readme`

We get back the password for the next level which is:

flag: **IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x**
