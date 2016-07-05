In this level we're given another **setuid** executable.
We're told to run it with a port and it'll execute as bandit 21
listening on the given port. It'll send us the password for bandit 21
if we supply it with the password for bandit 20.
The problem is that after running the `suconnect` executable, we cannot
use `nc` to communicate with the port we supplied in the same window.
We overcome this by making 2 terminal windows.


In the first terminal window

1) `./suconnect 23232`  This can be almost any port as long as we're consistent.


In the second terminal we run `nc` with the `-l` flag so it should remain and listen as oppose to shut the connection after running.

2) `nc -l 127.0.0.1 23232`

We then send the password for the previous level and get the flag. Window 1 Looks as follows:

    bandit20@melinda:~$ ./suconnect 12345
    Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
    Password matches, sending next password

While window 2 with out flag looks like:

    bandit20@melinda:~$ nc -l 12345
    GbKksEFF4yrVs6il55v6gwY5aVje5f0j
    gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

Flag: **gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr**
