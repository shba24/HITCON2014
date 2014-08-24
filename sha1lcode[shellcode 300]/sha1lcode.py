#!/usr/bin/python

import sys,os
import struct

fp = open("in","wb+")

buff = struct.pack("<I",0x000003e8)
buff += "B"*16000

fp.write(buff)
fp.close()