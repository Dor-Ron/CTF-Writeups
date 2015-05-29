We need to find the access key for when we run gas.py
We know the person's name is Richard Stallman.
On line 117 we find the line we actually care about:

<code>  grades[max(grades.keys())+1] = {"name": name, "accesskey": hashlib.md5(name).hexdigest(), "grades": usergrades} </code>

We can see that the value for the accesskey is just the md5 hash of the user's name.
So we take the md5 hash of Richard Stallman (*956ae5688879015fa8a3f06b0056c10e*)
Enter it and get out the following:

command: login 956ae5688879015fa8a3f06b0056c10e
Login successful. Now logged in as "Richard Stallman". For help run "help".
command: help
-- GAS Authenticated Help --
view: view your grades
help: print this help
command: view
Your grades are:
Free Software: F
Spanish: A
Precalculus: A
theflagis: sta11man_g3ts_g00d_grad3s!
English: A
Chemistry: A
History: A
command:

Flag: sta11man_g3ts_g00d_grad3s!
