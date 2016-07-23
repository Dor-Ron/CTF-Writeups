**Problem**
-------------

	x = raw_input("enter the password: ");
	y = "";
	for c in x:
		y += chr(ord(c) ^ 14);
		if y == "ko}wmzhugQocQoQhbois":
			print "congratz the flag is " + y;
		else:
			print "nope";


**Solution**
------------

The most important line(s) in the code above are `y += chr(ord(c) ^ 14)` and `if y == "ko}wmzhugQocQoQhbois"` The first tells us what happens to our input,
and the second tell us what our imput needs to equal in order to get the flag. `chr()` returns a character from its ascii value. And `ord()` returns an ascii
value from it's character form. `^` is python's bitwise exclusive or operator, otherwise known as **XOR** . Getting the flag is really easy, we just need to know 
how XOR works. In XOR:

	a ^ b = c

So

	c ^ b = a

and 

	c ^ a = b

In our case this translates to:

	ord(c) ^ 14 = letter_from_"ko}wmzhugQocQoQhbois"

So,

	letter_from_"ko}wmzhugQocQoQhbois" ^ 14 = ord(c)

And if we'd do this for each letter, we'd eventually get the string required to run by our encryption algorithm in order to end up with "ko}wmzhugQocQoQhbois".
Luckily, we don't have to do it manually we just put it all in a for-loop. I did exactly that in the file *reversing.py* So give it a quick look.

Flag: **easyctf{i_am_a_flag}**
