import os,sys,zipfile
from os import listdir
from os.path import isfile, join,isdir
import magic
import subprocess



original_file = "tarmful-3f13b82f7794de783adfd6fa9928ad2c.zip"

onlyfiles = [ f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(),f)) ]
print onlyfiles
 
i = 1024

while i>=0:
	p = subprocess.Popen(["file",original_file],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	output = p.stdout.read()
	print output
	if ".zip" in original_file or "Zip" in output:
		os.system("unzip "+original_file)
	elif ".tar.gz" in original_file or "gzip compressed data" in output:
		os.system("tar -zxvf "+original_file)
	elif ".gz" in original_file or "gzip compressed data" in output :
		os.system("unzip "+original_file)
	elif ".tar.bz2" in original_file or "bzip2" in output:
		os.system("tar xvjf "+original_file)
	elif ".tar" in original_file or "tar archive" in output:
		os.system("tar xvf " +original_file)
	i-=1
	hello = [f for f in listdir(os.getcwd()) if isdir(join(os.getcwd(),f))]
	print hello
	os.chdir(os.getcwd()+"/"+hello[0].encode('string-escape'))
	onlyfiles=[]
	onlyfiles = [ join(os.getcwd(),f) for f in listdir(os.getcwd()) if isfile(join(os.getcwd(),f)) ]
	print onlyfiles
	original_file = onlyfiles[0].encode('string-escape')