#!/usr/bin/python

import os,sys
import struct

sys.setrecursionlimit(15000000)

fd = open("output.txt","wb+")
fk = open("hop.exe","r")
fk.seek(0x400)
baseaddr = 0x401000

text1 = fk.read()
text = text1[:]

set1 = ['0x401615', '0x401c26', '0x401da0', '0x401dff', '0x402049', '0x40240c', '0x40266a', '0x402721', '0x402a7f', '0x402eb0', '0x403016', '0x403215', '0x403375', '0x403417', '0x403472', '0x403555', '0x4035f0', '0x403a0c', '0x403cde', '0x403d07', '0x403d82', '0x40404c', '0x4051f4', '0x405320', '0x405c15', '0x405cdf', '0x406111', '0x40693c', '0x40840c', '0x40864f', '0x4093aa', '0x409ef1', '0x40a2ba', '0x40a622', '0x40a7ff', '0x40b6ee', '0x40b96d', '0x40ba89', '0x40badb', '0x40bbdc', '0x40be14', '0x40bf07', '0x40c6bb', '0x40c6e0', '0x40c7f0', '0x40cb09', '0x40cee3', '0x40cf6e', '0x40d33b', '0x40db04', '0x40def8', '0x40e1ae', '0x40e2f4', '0x40e9e0', '0x40eb93', '0x40fa9c', '0x40fd96', '0x411bc7', '0x411ce1', '0x411ef1', '0x412066', '0x41215e', '0x412345', '0x412821', '0x41380d', '0x413c72', '0x41530f', '0x41557a', '0x415e98', '0x4160a1', '0x416163', '0x41629e', '0x41649a', '0x416a3a', '0x4188fe', '0x41897e', '0x4189dc', '0x41967e', '0x41979b', '0x41a032', '0x41a6d2', '0x41a718', '0x41a89f', '0x41b21d', '0x41b307', '0x41b4dd', '0x41bf19', '0x41d1fb', '0x41da73', '0x41dca8', '0x41e38b', '0x41e42b', '0x41e443', '0x41e9e0', '0x41ec61', '0x41f740', '0x41fc82', '0x420131', '0x42017a', '0x420559', '0x421573', '0x4220c1', '0x4221da', '0x42230f', '0x42232d', '0x422375', '0x4246ee', '0x424df4', '0x425143', '0x425933', '0x4259ef', '0x42660b', '0x4266c7', '0x42689d', '0x426a2b', '0x426d0f', '0x426df9', '0x42724a', '0x427551', '0x427dbb', '0x428af7', '0x42922f', '0x4298d6', '0x429b0f', '0x429f57', '0x42a071', '0x42a2ef', '0x42a8f9', '0x42aa39', '0x42b3a6', '0x42bcfc', '0x42c711', '0x42cba0', '0x42dadb', '0x42ea43', '0x42ea6a', '0x42f016', '0x42f0e2', '0x42f618', '0x42fb88', '0x4300f7', '0x430da8', '0x43125d', '0x431500', '0x431546', '0x432a95', '0x4331a8', '0x433229', '0x43495a', '0x4359d6', '0x4367b9', '0x4373bb', '0x43783d', '0x437a5b', '0x437c96', '0x437d20', '0x438154', '0x4388c7', '0x43970e', '0x439d43', '0x43a257', '0x43a28a', '0x43a8fb', '0x43ab29', '0x43b2f2', '0x43c65d', '0x43ca9c', '0x43cdb0', '0x43d593', '0x43d8d2', '0x43dbd2', '0x43dd53', '0x43dd70', '0x43e01f', '0x43e3bc', '0x43f3d7', '0x43f5b3', '0x43f8ab', '0x43ff24', '0x440649', '0x44095f', '0x440c3a', '0x4415d4', '0x441e22', '0x442674', '0x443203', '0x4439ca', '0x44436d', '0x4444ad', '0x44502d', '0x445335', '0x446557', '0x446605', '0x446b96', '0x446cc7', '0x446e27', '0x44718f', '0x448ae9', '0x44a10a', '0x44a7c6', '0x44bfdf', '0x44c59d', '0x44c75b', '0x44cb54', '0x44cd15', '0x44ce8f', '0x44d97e', '0x44d9ec', '0x44dc04', '0x44e4a6', '0x44e975', '0x44ee89', '0x44eea2', '0x44ef7c', '0x44f326', '0x44f3fc', '0x44f491', '0x44fd11', '0x44fec2', '0x4527de', '0x452e52', '0x45340d', '0x453761', '0x4548b9', '0x455d0b', '0x456440', '0x456b39', '0x4571d7', '0x4577af', '0x4588eb', '0x458ed6', '0x4591c0', '0x45963c', '0x45a2d9', '0x45a3cc', '0x45aed3', '0x45b804', '0x45b95f', '0x45c4c5', '0x45c7c1', '0x45d37c', '0x45d755', '0x45d7fd', '0x45db97', '0x45e06d', '0x45e881', '0x45f705', '0x4608dc', '0x46244d', '0x46250d', '0x46270e', '0x462cc8', '0x4632e0', '0x463d22', '0x4640c7', '0x4647c4', '0x4666cf', '0x4675fd', '0x46774a', '0x4679f0', '0x467d0f', '0x468585', '0x4696be', '0x469f29', '0x46a41d', '0x46a7ec', '0x46aced', '0x46b03e', '0x46b177', '0x46b5b2', '0x46c19f', '0x46d48a', '0x46d4de', '0x46e08e', '0x46e2ec', '0x46e455', '0x46e874', '0x46ef51', '0x46f4bd', '0x46fc89', '0x47054e', '0x4707cb', '0x471bf2', '0x4724fd', '0x472c7e', '0x47337d', '0x4735f4', '0x473a8c', '0x4745db', '0x4747bf', '0x474dfc', '0x474ed0', '0x4750d7', '0x4758f4', '0x475bd8', '0x475bf3', '0x475d54', '0x475fd2', '0x476d3c', '0x476ea2', '0x476f2a', '0x47783a', '0x477d97', '0x4785e0', '0x47882f', '0x47931f', '0x479376', '0x4799b4', '0x479dd5', '0x47a6c4', '0x47aa92', '0x47adca', '0x47aed3', '0x47b186']
set2 = []
set3 = []
graph1 = {}
graph = {}

def add_to_char(answer):
	n = 0
	for i in answer:
		if n==0:
			pst= i
		else:
			for k in graph1[pst]:
				if k[1]==i:
					pst = i
					print k[0],
		n+=1
	print ""

def parse_tree(text):
	flag = 0
	for i in text:
		if "==>" in i:
			if flag==0:
				rdx = i[3:].split()[0]
				lst = set()
				lst1 = set()
				common = set()
				flag = 1
			else:
				if len(lst)!=0:
					#print common
					graph1[rdx] = lst1
					lst = lst - common
					graph[rdx] = lst
					set2.append(rdx)
					#print rdx,len(lst)
					rdx = i[3:].split()[0]
				lst = set()
				lst1 = set()
				common = set()
		elif "->" in i and ord(i[0])<=0x7f and ord(i[0])>=0x20 :
			address = i.split("->")[1][:-1]
			tmp = set()
			tmp.add(address)
			if tmp.issubset(lst)==False:
				lst1.add((i[0],address))
				lst.add(address)
			else:
				common.add(address)
	if len(lst)!=0:
		#print common
		lst =lst - common
		set2.append(rdx)
		#print rdx,len(lst)
		graph1[rdx] = lst1
		graph[rdx] = lst
	#print set2

def bfs(graph,start,end):
	queue = []
	queue.append([start])
	while queue:
		path = queue.pop(0)
		vertex  = path[-1]
		if vertex==end and len(path)>=0x20:
			add_to_char(path)
			return path
		#print vertex
		for adjacent in list(graph[vertex]):
			new_path = list(path)
			new_path.append(adjacent)
			if adjacent==end and len(new_path)>=0x20 :
				add_to_char(new_path)
				return new_path
			queue.append(new_path)
	return None

flg = 0
index = text.find("\x8b\x84\x02")
while text[index-8:index-4]!="\x58\x48\x69\xc0":
	text = text[index+3:]
	baseaddr+=(index+3)
	#print index
	index = text.find("\x8b\x84\x02")
#print index
flg = 1
while flg==1:
	gap = struct.unpack("<I",text[index-4:index])[0]
	start = index+baseaddr-8
	gap_1 = struct.unpack("<I",text[index+3:index+7])[0]
	set3.append(hex(start))
	fd.write("==>"+hex(start)+" "+hex(gap)+" "+hex(gap_1)+"\n" )
	n = 0
	for k in xrange(0x20,0x7f):
		off = start+gap_1+(gap*k)
		off1 = struct.unpack("<i",text1[off-0x401000:off-0x401000+4])[0]
		if (hex(off1 + start)) in set1:
			fd.write(chr(k)+"->"+hex(off1 + start)+"\n")
			n+=1
	if n==0x7f:
		print start
	text = text[index+9:]
	baseaddr+=(index+9)
	flg = 0
	index = text.find("\x8b\x84\x02")
	while index!=-1 and text[index-8:index-4]!="\x58\x48\x69\xc0":
		text = text[index+3:]
		baseaddr+=index
		index = text.find("\x8b\x84\x02")
	if index!=-1:
		flg = 1
#print set3
fd.close()
fd = open("output.txt","r")
text = fd.readlines()
parse_tree(text)
#print graph

bfs(graph, "0x43a8fb", "0x46fc89")
#for i in list(set3):
#	print i
#	answer = bfs(graph,i,"0x46fc89")
#	answer = bfs(graph,i, i)
#answer = bfs(graph,"0x44f491","0x44f491")
#print len(answer)