First we find out which ports are open from range 31000-32000, we do that by:

`nmap --open 127.0.0.1 -p 31000-32000`

This returns 5 ports:

    PORT      STATE Service
    31046/tcp open  unknown
    31518/tcp open  unknown
    31691/tcp open  unknown
    31790/tcp open  unknown
    31960/tcp open  unknown

Now we need to fill in the service column for the 5 ports by doing:

`nmap 127.0.0.1 -p 31046,31518,31691,31790,31960`

and get back:

    Starting Nmap 5.21 ( http://nmap.org ) at 2014-07-31 20:13 UTC
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.00076s latency).
    Not shown: 995 closed ports
    PORT      STATE SERVICE VERSION
    31046/tcp open  echo
    31518/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
    31691/tcp open  echo
    31790/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
    31960/tcp open  echo
    Service Info: OSs: Linux, Windows

    Service detection performed. Please report any incorrect results at http://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 41.19 seconds

We don't care for the echo ports, so that only really leaves us with ports: **31518** and **31790**.
Following the previous level, to connect through ssl we do:

`cat /etc/bandit_pass/bandit16 | openssl s_client -connect 127.0.0.1:31518 -quiet`

This unfortunately was not that one returning:

    depth=0 CN = localhost
    verify error:num=18:self signed certificate
    verify return:1
    depth=0 CN = localhost
    verify return:1
    cluFn7wTiGryunymYOu4RcffSxQluehd

So we try the only remaining port:

`cat /etc/bandit_pass/bandit16 | openssl s_client -connect 127.0.0.1:31790 -quiet`

Which returns an rsa key we'll need to connect to bandit17

    depth=0 CN = localhost
    verify error:num=18:self signed certificate
    verify return:1
    depth=0 CN = localhost
    verify return:1
    Correct!
    -----BEGIN RSA PRIVATE KEY-----
    MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
    imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
    Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
    DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
    JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
    x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
    KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
    J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
    d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
    YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
    vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
    +TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
    8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
    SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
    HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
    SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
    R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
    Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
    R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
    L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
    blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
    YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
    77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
    dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
    vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
    -----END RSA PRIVATE KEY-----

    read:errno=0

To proceed to the next level:

Copy the RSA key into a new file, so:

`mkdir /tmp/<enter_dir_name> && cd /tmp/<enter_dir_name>`

then:

`touch sshkey.private && nano sshkey.private`

Paste the file and **^X**

We need to change the permissions for the file too, otherwise we'll get an error saying that *Permissions 0664 for 'sshkey.private' are too open.* when we try to `ssh -i`

So to fix this:

`chmod 600 sshkey.private`

and finally!

`ssh -i sshkey.private bandit17@localhost`
