1) `ssh bandit12@bandit.labs.overthewire.org` and put the password for the level

2)`ls -a` to show all the files, we're get back:

    .  ..  .bash_logout  .bashrc  .profile  data.txt
  
We care about data.txt, I won't run `file` on it because obviously it's a text file.

3) `cat data.txt | grep "password"` or `strings`, we can't find the password, but the output looks like a hexdump.

We want to use `xdd` from the suggested commands to decompile the hexdump, but we need write access, so we make a folder under tmp.

4) `mkdir /tmp/idk-bruh && cp data.txt /tmp/idk-bruh && cd /tmp/idk-bruh`

Now that the file is in our temporary folder, and so are we, let's read the `man xxd`

5) `xxd -r data.txt > reverse_hd`  decompiled file will be named reverse_hd

6) `file reverse-hd` to check what we're dealing with, get back:

    reverse_hd: gzip compressed data, was "data2.bin", from Unix, last modified: Fri Nov 14 10:32:20 2014, max compression

The next steps are basically just repeated similar commands so I will skip explanations, as they should be obvious.

    bandit12@melinda:/tmp/idk-bruh$ gzip -cd reverse_hd > reverse_gzip
    bandit12@melinda:/tmp/idk-bruh$ file reverse_gzip 
    reverse_gzip: bzip2 compressed data, block size = 900k
    bandit12@melinda:/tmp/idk-bruh$ bzip2 -cd reverse_gzip > reverse_bzip2
    bandit12@melinda:/tmp/idk-bruh$ file reverse_bzip2 
    reverse_bzip2: gzip compressed data, was "data4.bin", from Unix, last modified: Fri Nov 14 10:32:20 2014, max compression
    bandit12@melinda:/tmp/idk-bruh$ gzip -cd reverse_bzip2 > reverse_gzip_2
    bandit12@melinda:/tmp/idk-bruh$ file reverse_gzip_2 
    reverse_gzip_2: POSIX tar archive (GNU)
    bandit12@melinda:/tmp/idk-bruh$ tar -xf reverse_gzip_2
    bandit12@melinda:/tmp/idk-bruh$ ls
    data.txt  data5.bin  reverse_bzip2  reverse_gzip  reverse_gzip_2  reverse_hd
    bandit12@melinda:/tmp/idk-bruh$ file data5.bin 
    data5.bin: POSIX tar archive (GNU)
    bandit12@melinda:/tmp/idk-bruh$ tar -xf data5.bin 
    bandit12@melinda:/tmp/idk-bruh$ ls
    data.txt  data5.bin  data6.bin  reverse_bzip2  reverse_gzip  reverse_gzip_2  reverse_hd
    bandit12@melinda:/tmp/idk-bruh$ file data6.bin
    data6.bin: bzip2 compressed data, block size = 900k
    bandit12@melinda:/tmp/idk-bruh$ bzip2 -cd data6.bin > howmanymore
    bandit12@melinda:/tmp/idk-bruh$ file howmanymore 
    howmanymore: POSIX tar archive (GNU)
    bandit12@melinda:/tmp/idk-bruh$ tar -xf howmanymore
    bandit12@melinda:/tmp/idk-bruh$ ls
    data.txt  data5.bin  data6.bin  data8.bin  howmanymore  reverse_bzip2  reverse_gzip  reverse_gzip_2  reverse_hd
    bandit12@melinda:/tmp/idk-bruh$ file data8.bin 
    data8.bin: gzip compressed data, was "data9.bin", from Unix, last modified: Fri Nov 14 10:32:20 2014, max compression
    bandit12@melinda:/tmp/idk-bruh$ gzip -cd data8.bin > cmonbro
    bandit12@melinda:/tmp/idk-bruh$ file cmonbro 
    cmonbro: ASCII text
    bandit12@melinda:/tmp/idk-bruh$ cat cmonbro 
    The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

Flag: **8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL**
