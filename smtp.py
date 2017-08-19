#!/usr/bin/env python
import smtplib

server=smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("yanivcohen80", "40229239")

msg = "This is a test with smtp lib and gmail"
server.sendmail("yanivcohen80@gmail.com","yaniv4345@gmail.com",msg)
server.quit()
