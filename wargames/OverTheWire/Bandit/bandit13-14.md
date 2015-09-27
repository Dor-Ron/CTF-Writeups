1) `ssh bandit13@bandit.labs.overthewire.org` and enter the password

2) `ls -a` returns:

  sshkey.private
  
I tried `ssh -i sshkey.private bandit14@bandit.labs.overthewire.org` but that didn't work, we needed:

3) `ssh -i sshkey.private bandit14@localhost`

Flag: No flag for this level we just get thrown into bandit14
