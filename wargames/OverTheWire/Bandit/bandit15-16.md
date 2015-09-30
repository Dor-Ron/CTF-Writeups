`cat /etc/bandit_pass/bandit15 | openssl s_client -connect 127.0.0.1:30001 -quiet`

Get the password, pipe, then use ssl encryption using a client to connect to localhost on port 30001,
-quiet cause we're instructed.
