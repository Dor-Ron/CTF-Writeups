If you didn't already know by looking at the information, the file name **rsa.txt**
Should've given it away. We need to decrypt the message. We add **0x** in front of text, d, and n
to denote a hexadecimal in python. We then use the pow function to text ^ d % n.
Convert that number into a hexadecimal again and decode it leaving out the Ox and the L added by python.

Flag: stuyctf{rsa_large_primes_4_security}
