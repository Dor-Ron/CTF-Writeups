We're told there's a cronjob running, so we check out our cronjob by:

1) `cd /etc/cron.d  && ls -al`

    total 128
    drwxr-xr-x   2 root root 4096 Jul 22 13:40 ./
    drwxr-xr-x 109 root root 4096 Jul 31 13:19 ../
    -rw-r--r--   1 root root  102 Apr  2  2012 .placeholder
    -rw-r--r--   1 root root   52 Oct 22  2013 boobiesbot-check
    -rw-r--r--   1 root root  355 Nov 18  2011 cron-apt
    -rw-r--r--   1 root root   61 Jun  6  2013 cronjob_bandit22
    -rw-r--r--   1 root root   62 Jun  6  2013 cronjob_bandit23
    -rw-r--r--   1 root root   61 Jun  6  2013 cronjob_bandit24
    -rw-r--r--   1 root root   35 Jun  6  2013 eloi0
    -rw-r--r--   1 root root   35 Jun  6  2013 eloi1
    -rw-r--r--   1 root root   49 Jul  3 14:13 hintbot-check
    -rw-------   1 root root  233 Jun  6  2013 manpage3_resetpw_job
    -rw-r--r--   1 root root   51 Jul 12 15:57 melinda-stats
    -rw-r--r--   1 root root   54 Sep 30  2013 natas-session-toucher
    -rw-r--r--   1 root root   49 Sep 30  2013 natas-stats
    -r--r-----   1 root root   47 Sep 30  2013 natas25_cleanup
    -r--r-----   1 root root   45 Jul 22 13:40 natas26_cleanup
    -rw-r--r--   1 root root  544 Mar 11  2013 php5
    -rw-r--r--   1 root root   58 Jun  6  2013 semtex0-32
    -rw-r--r--   1 root root   58 Jun  6  2013 semtex0-64
    -rw-r--r--   1 root root   59 Jun  6  2013 semtex0-ppc
    -rw-r--r--   1 root root   36 Jun  6  2013 semtex10
    -rw-r--r--   1 root root  143 Jun  6  2013 semtex12
    -rw-r--r--   1 root root   35 Jun  6  2013 semtex5
    -rw-r--r--   1 root root   29 Jun  6  2013 semtex6
    -rw-r--r--   1 root root   96 Jun  6  2013 semtex8
    -rw-r--r--   1 root root  134 Jun  6  2013 semtex9
    -rw-r--r--   1 root root  396 Dec 16  2011 sysstat
    -rw-r--r--   1 root root   29 Jun  6  2013 vortex0
    -rw-r--r--   1 root root   30 Jul  2  2013 vortex20
    -rw-r--r--   1 root root   52 Jul  3 13:41 vulnbot0-check
    -rw-r--r--   1 root root   52 Jul  3 13:41 vulnbot1-check

The won we care about is **cronjob_bandit22** so we check it out

2) `cat cronjob_bandit22`

    * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

We can see that there's a corresponding script stored in **/usr/bin/**

3) `cd /usr/bin`

Now we checkout the script we care about

4) `cronjob_bandit22.sh`

    #!/bin/bash
    chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
    cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

We see that the cronjob put's bandit 22 in a file called **t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv** in out **tmp** directory. So let's check it out

5) `cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`

Flag: **Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI**
