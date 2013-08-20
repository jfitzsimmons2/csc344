#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  process.py
#  

import os
import zipfile
import glob

def summarize(filename,directory):
	validlines = 0
	if directory == 'a1' or directory == 'a3' or directory == 'a4':
		with open(filename) as f:
			dontcount = 0
			count = 0
			comment = False
			for line in f:
				line = line.strip()
				if line == "":
					#print('n ' + line)
					dontcount += 1
					count += 1
				elif line.startswith('/*') and line.endswith('*/'):
					#print('n ' + line)
					dontcount += 1
					count += 1
				elif line.startswith('/*'):
					comment = True
					#print('n ' + line)
					dontcount += 1
					count += 1
				elif line.endswith('*/'):
					comment = False
					#print('n ' + line)
					dontcount += 1
					count += 1
				elif comment == True:
					#print('n ' + line)
					dontcount += 1
					count += 1
				else:
					#print('y ' + line)
					count += 1
					
			validlines = count - dontcount		
			return validlines
	elif directory == 'a2':
		with open(filename) as f:
			count = 0
			dontcount = 0
			for line in f:
				line = line.strip()
				if line.startswith(';'):
					#print('n ' + line)
					dontcount += 1
					count += 1
				elif line == '':
					#print('n ' + line)
					dontcount += 1
					count += 1
				else:
					#print('y ' + line)
					count += 1
			return (count - dontcount)
	elif directory == 'a5':
		if filename == '__pycache__':
			print("dont need pycache")
		else:
			with open(filename) as f:
				count = 0
				dontcount = 0
				for line in f:
					line = line.strip()
					if line.startswith('#'):
						#print('n ' + line)
						dontcount += 1
						count += 1
					elif line == '':
						#print('n ' + line)
						dontcount += 1
						count += 1
					else:
						#print('y ' + line)
						count += 1
				return (count - dontcount)
				
def makezip(paths):
	zf = zipfile.ZipFile("CSC344-JoeFitzsimmons.zip", "w")
	
	for path in paths:
		for i in path:
			zf.write(i)
	
	zf.write(glob.glob('*.html')[0])
	zf.close()
			
