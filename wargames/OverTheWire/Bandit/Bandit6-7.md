#Bandit Level 6 → Level 7
-------------------------

Getting lazy, so I'm just gonna do these from one file from now on...

**Problem**
The password for the next level is stored *somewhere on the server* and has all of the following 
properties: - owned by user bandit7 - owned by group bandit6 - 33 bytes in size

**Solution**

Somewhere on this server implies we need to go all the way back to the root directory so:

`cd /`

We need to find a file so we'll use the `find` bash command:

`find / -user bandit7 -group bandit6 -size 33c`

Means search all the branches for a file owned by bandit7 and group bandit6 of size 33 bytes.

We get back a bunch of permission denied messsages but luckily one is reassuring.

`/var/lib/dpkg/info/bandit7.password`

So now we do:

`cd /var/lib/dpkg/info/ && cat bandit7.password`

Flag: **HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs**
