from hexdump import hexdump
import struct

Q = lambda x: struct.unpack("I", x)[0]

# flag is 40 long

ks = []
#ks += map(chr, range(ord('0'), ord('9')+1))
#ks += map(chr, range(ord('A'), ord('Z')+1))
#ks += map(chr, range(ord('a'), ord('z')+1))
#ks += list("{}_")
ks = map(chr, range(1, 0x80))

dat = "\x00"*0xC00+open("hop-62fa7ade9a1fa9254361e69d70e7a7e3.exe").read()
print "0x1590 = 0x%X" % dat.find("\xb8\x28\x00\x00\x00\x6a\x00\x48\xff\xc8")
hexdump(dat[0x1590:][0:0x10])


def visit(ptr):
  global ntargets, ngoodstates
  jumper = Q(dat[ptr+4:ptr+4+4])
  liloff = Q(dat[ptr+11:ptr+11+4])
  zptr = ptr + Q(dat[ptr+liloff:ptr+liloff+4])

  #print "at %8X %8X %8X z%8x %s" % (ptr,jumper,liloff,zptr,dat[ptr:ptr+0x16].encode("hex"))
  for c in ks:
    target = ptr + ord(c)*jumper + liloff
    dtarget = (ptr + Q(dat[target:target+4])) & 0xFFFFFFFF
    ntargets.append((dtarget,c,ptr))

# start state is 0x4f491
goodstates = [0x6EF51]
strlen = 41
targets = [(0x4f491, "\x00")]   # targets are everything this round can branch to
#strlen = 40-7
#targets = [(0x29f57, "\x00")]   # targets are everything this round can branch to
donetargets = []

rtargets = []

# get the targets for each round
for i in range(strlen):
  print "round",i
  rtargets.append(targets)
  ntargets = []
  if i==1 or i==0:
    print targets[0][0]+0x400000
  for t in set(map(lambda x: x[0], targets)):
    #print t,
    visit(t)
    donetargets.append(t)
  targets = ntargets


vchars = []

# work backward to solve
for i in range(strlen-1,0,-1):
  print "round",i
  ngoodstates = []
  vchar = []
  for (t,c,ptr) in rtargets[i]:
    if t in goodstates:
      print c,hex(ptr),"->",hex(t)
      vchar.append(c)
      ngoodstates.append(ptr)
  goodstates = ngoodstates
  vchars.append(vchar)


flag = ""
for vc in vchars[::-1]:
  flag += vc[0]

print flag
