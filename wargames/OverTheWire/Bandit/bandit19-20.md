`ls` returns:

`bandit20-do`

cool, running the executable

`./bandit20-do` returns:

    Run a command as another user.
      Example: ./bandit20-do id

Great! We can run a command as bandit20, in other words we can see the password for that level needed to ssh into it.

`./bandit20-do cat /etc/bandit_pass/bandit20`

This returns our flag:

Flag: **GbKksEFF4yrVs6il55v6gwY5aVje5f0j**
