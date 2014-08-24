#!/usr/bin/python -u

import os
import ctypes
import sys
import code
import time


inspect_flag = 321 
if __name__ == '__main__':

	print hex(id(inspect_flag))
	c = ctypes.CDLL("libc.so.6")
	c.printf("hello world!\n")
	c.printf("who are U?\n")
	name = os.sys.stdin.readline()

	_len = len(name)
	print _len
	#_f = open('/proc/self/mem','r+')
	#_f.seek(0x00007fff74c33000-_len)
	#_f.write(name.strip())
	#_f.close()

	name = "hi! " + name + "bye!\n"
	c.printf(name)

if inspect_flag >321 :
	vars = globals().copy()
	vars.update(locals())
	shell = code.InteractiveConsole(vars)
	shell.interact()

