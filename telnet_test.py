#!/usr/bin/env python
import socket
import time
import base64
HOST='10.0.0.7'
PORT=25
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
ehlo = "ehlo wtf.org.il\r\n"
s.sendall(ehlo)
fro = "mail from: yaniv@wtf.org.il\r\n"
s.sendall(fro)
rcpt = "rcpt to: yaniv4345@gmail.com\r\n"
s.sendall(rcpt)
data = "data\r\n"
s.sendall(data)
subject = "Subject: This is a test\r\n"
s.sendall(subject)
msg = "\nblabla\r\n"
s.sendall(msg)
end = ".\r\n"
s.sendall(end)
data=s.recv(1024)
s.close()
print "Recived:\n", repr(data)

