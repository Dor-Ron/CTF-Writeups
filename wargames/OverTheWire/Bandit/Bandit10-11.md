#Bandit Level 10 → Level 11

**Problem**

The password for the next level is stored in the file data.txt, which contains base64 encoded data

**Solution**

1) `ls -a`  -  to make sure I'm in the same directory as data.txt

2) `base64 -d data.txt`  -  `base64 -d` to decode the file with base64 obviously

**OUTPUT**

    The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
    
Flag: **IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR**
