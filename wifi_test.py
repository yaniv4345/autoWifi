#!/usr/bin/env python
from wifi import Cell, Scheme
import ping
import os
import time
import socket
import netifaces as ni
iface="wlan0"
def sendEmail(ssid,address):
    HOST='wtf.org.il'
    PORT=10000
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
    subject = "Subject: New wifi connect\r\n"
    s.sendall(subject)
    msg = "\nNew wifi connection\n"
    msg = msg + "SSID: " + ssid +  "\n"
    msg = msg + "IPADDRESS: " + address + "\r\n"
    s.sendall(msg)
    end = ".\r\n"
    s.sendall(end)
    data=s.recv(1024)
    s.close()
def connect():
    cells = Cell.all(iface)
    for cell in cells:
        if cell.encrypted == False:
            ssid = cell.ssid
            try:
                # Did not found ssid in file trying to connect
                scheme=Scheme.for_cell(iface, cell.ssid, cell)
                scheme.save()
                scheme.activate()
            except:
                # Try to find the ssid in /etc/network/interfaces
                scheme=Scheme.find(iface, cell.ssid)
                scheme.activate()
        time.sleep(2)
        response=ping.do_one('www.google.com', 1, 64)
        if response > 0:
            address=ni.ifaddresses('wlan0')[2][0]['addr']
            sendEmail(ssid, address)
            break
        else:
            continue
connect()
