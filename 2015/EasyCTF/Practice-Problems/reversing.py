#!/usr/bin/python

#Encryption

'''
x = raw_input("enter the password: ");
y = "";
for c in x:
	y += chr(ord(c) ^ 14);
	if y == "ko}wmzhugQocQoQhbois":
		print "congratz the flag is " + y;
	else:
		print "nope";
'''

#Decryption
#Also, who the fuck uses semicolons in python??

flag = ""
encrypted = "ko}wmzhugQocQoQhbois"
for letter in encrypted:
	flag += chr(ord(letter) ^ 14)

print flag #=> easyctf{i_am_a_flag}
