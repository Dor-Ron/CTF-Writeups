#Bandit Level 11 → Level 12

**Problem**

The password for the next level is stored in the file data.txt, 
where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

**Solution**

1) `ls -a`  -  to make sure *data.txt* is in the directory.

2) `python`  -  Activate python REPL

3) In python:

    import os
    
    string_to_decode = os.popen('data.txt').read()
    
    string_to_decode.decode('rot13')

**OUTPUT**

`u'The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu\n'`

Flag: **5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu**
