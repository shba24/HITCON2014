#!/usr/bin/python

import os,sys
import struct

fk = open("hop.exe","r")

## pivot the file pointer to .text section
fk.seek(0x400)

## base address of .text section
baseaddr = 0x401000

text = fk.read()

## array of all printable ascii characters
characters = map(chr, xrange(1,0x80))

## starting address of the graph
start = 0x44f491
## ending address of the graph
end = 0x46ef51

flag = []
## flag length is 41 including "\x00" at end
flag_len = 41

## function to find the all adjacent nodes/ branch nodes of a node
def travel(addr):
	global alltarget
	gap = struct.unpack("<I",text[addr-baseaddr+4:addr-baseaddr+8])[0]
	jump = struct.unpack("<I",text[addr-baseaddr+11:addr-baseaddr+15])[0]
	for i in characters:
		mem = addr + (gap*ord(i)) + jump
		#print hex(mem),i,hex(addr),hex(gap),hex(jump)
		dest = struct.unpack("<I",text[mem-baseaddr:mem-baseaddr+4])[0]
		dest = (dest + addr) & 0xffffffff
		alltarget.append((addr,i,dest))

target_addr = [(start,"\x00",start)]

## stage_target will content list of list of possible accessible nodes at each stage
stage_target = []
for i in xrange(flag_len):
	stage_target.append(target_addr)
	alltarget = []
	### loop for finding all possible accessible nodes at stage i
	for j in set(map(lambda a:a[2],target_addr)):
		travel(j)
	target_addr = alltarget

follow = end
### Backtracing the possible path from end to start
for i in xrange(flag_len-1,-1,-1):
	for (addr,j,dest) in stage_target[i]:
		if dest == follow:
			goodones = addr
			flag.append(j)
			print j,hex(dest) +"->"+hex(addr)
	follow=goodones

## Final FLag
print "".join(flag[-1::-1])