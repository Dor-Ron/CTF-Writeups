You should still be connected to the bandit0 remote host over ssh.
In the directory we're directed to when we first connect, we use the `ls` command,
and see that there is one file in the directory called **readme**.
We then view the contents of **readme** using `cat readme`, and we're shown th following.

*boJ9jbbUNNfktd78OOpsqOltutMc3MY1*

We are told that is the password to accesss the bandit1 remote host. So we run `exit` to leave bandit0.
Back at our local machine we run `ssh bandit1@bandit.labs.overthewire.org`, and when prompted for the password we
type in *boJ9jbbUNNfktd78OOpsqOltutMc3MY1*. We should then get the default welcome message signifying that we've
successfully completed bandit1.
