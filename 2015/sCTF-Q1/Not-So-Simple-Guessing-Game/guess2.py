#!/usr/bin/env python

import socket

for i in xrange(100): 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.connect(("python.sctf.io", 11235))
	response = s.recv(4096) 
	response = response.translate(None, "abcdefghijklmnopqrstuvwxyz ") 
	s.send(str(i)) 
	response2 = s.recv(4096)
	print response2 
