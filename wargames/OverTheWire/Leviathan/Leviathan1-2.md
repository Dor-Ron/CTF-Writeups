As for all Leviathan problems, the problem description is intentionally left blank.
So lets just get into it:

1) `ssh leviathan1@leviathan.labs.overthewire.org`   and enter the password **rioGegei8m**

2) `leviathan1@melinda:~$  ls -a`   to check all files & directories. Returns:

    .  ..  .bash_logout  .bashrc  .profile  check
    
3) `file check`   To check what type of file we're dealing with, returns: 

    check: setuid ELF 32-bit LSB  executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0d17ae20f672ebc7d440bb4562277561cc60f2d0, not str
    ipped
    
OK, so it's an executable, we'll try running it later if this doesn't work.

4) `strings check | grep "password"` and just `strings check`   To check if password was in the file.
doesn't really return anything to interesting. Looks like we're dealing with a C file though.

5) `./check`      Lets run the executable, prompts us for password, enter something random, get error.

6) `strace ./check` Let's try debugging this thing. We see it accepts 3 letters for input, but we can't narrow it down yet.

7) `ltrace ./check` Let's try tracing the executable with a different command. This time we see this line:

    strcmp("\n\n\n", "sex") 
    
strcmp() function compares to strings to check if they are equal. So we have to enter sex for the comparison to return true.

8) `./check`   Let's run the executable again.

    password: sex
    
No error this time, however, instead of **leviathan1@melinda:~$** we just have **$**

Ok, so then let's check if our user is still leviathan1

9) `whoami`    to check current user, returns:

    leviathan2
    
Alright, if we're leviathan2, we should be able to access the password for a level we *already* 'cleared'

10) `cd /etc/leviathan_pass && cat *`   show us all accessible leviathan passwords, returns:

    cat: leviathan0: Permission denied
    cat: leviathan1: Permission denied
    ougahZi8Ta
    cat: leviathan3: Permission denied
    cat: leviathan4: Permission denied
    cat: leviathan5: Permission denied
    cat: leviathan6: Permission denied
    cat: leviathan7: Permission denied
    
Flag: **ougahZi8Ta**
