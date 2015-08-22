#Bandit Level 8 → Level 9
=========================

**Problem**

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

**Solution**

`ls` to make sure we're in the same directory as *data.txt*, we are, let's continue.

We're looking for a unique line, excellent time to use `uniq`, but the way It's algorithm works
relies on that the file is sorted alphanumerically. So we'll pipe a few commands together.

`cat data.txt | sort | uniq -u`

Flag: **UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR**
