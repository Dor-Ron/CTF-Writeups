We are already told what we need to do to obtain the flag, which is to submit
The flag for bandit 14 to port 30000 on localhost, otherwise represented as 127.0.0.1
as all backend developers such as myself should know. So we do:

  `cat /etc/bandit_pass/bandit14 | nc 127.0.0.1 30000` could've used telnet instead of netcat but who cares?
  
We get back

  Correct!
  BfMYroe26WYalil77FoDi9qh59eK5xNr


Flag: **BfMYroe26WYalil77FoDi9qh59eK5xNr**
