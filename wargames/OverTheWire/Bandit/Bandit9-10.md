#Bandit Level 9 → Level 10

**Problem**

The password for the next level is stored in the file data.txt in one of the few human-readable strings, 
beginning with several ‘=’ characters.

**Solution**

1) `ls -a`  -  to make sure *data.txt* is in the directory

2) `strings data.txt | grep -w "="`  -  `strings` for the human readable requirement `grep -w "="` for 
words in *data.txt* that begin with an equal sign

**OUTPUT:**

    I========== the6
    ========== password
    ========== ism
    N$=&
    ========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
    
Flag: **truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk**
