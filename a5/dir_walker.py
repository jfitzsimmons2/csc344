#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dir_walker.py
#  

import os
import process

def take_a_walk():
	assignments = []
	assignmentsLineCount = []
	assignmentsLinks = []
	assignmentsFileNames = []
	directories = os.listdir(os.getcwd())
	for directory in directories:
		if directory.endswith('.html') or directory.endswith('.zip'):
			continue
		else:
			os.chdir(directory)
		links = list()
		lc = list()
		files = os.listdir(os.getcwd())
		for f in files:
			if f.endswith('.bat') or f.startswith('__'):
				continue
			else:
				links.append(directory + os.sep + f)
				lc.append(process.summarize(f,directory))
		os.chdir(os.pardir)
		assignmentsLineCount.append(lc)
		assignmentsLinks.append(links)
	assignments.append(assignmentsLineCount)
	assignments.append(assignmentsLinks)
	return assignments


