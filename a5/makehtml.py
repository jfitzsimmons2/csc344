#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  makehtml.py
#  

import main
import os

def write(datum):
	linecounts = datum[0]
	filelinks  = datum[1]
	html = open('csc344.html', '+w')
	html.write('<!doctype html')
	html.write('<html><head><title>CSC344 Assignments</title></head>')
	html.write('<body><h1>CSC344 Assignments</h1><hr />')

	number = 1
	index = 0
	for lc, links in zip(linecounts,filelinks):
		html.write('<h2>Assignment '+format(number)+'</h2>')
		number += 1
		html.write('<table border=0>')
		html.write('<tr><td><strong>Lines</strong></td>')
		html.write('<td><strong>File</strong></td></tr>')
		acc = 0
		for x, y in zip(lc, links):
			acc += x
			html.write('<tr><td>'+format(x)+'</td>')
			html.write('<td><a href="'+y+'">'+y+'</a></td></tr>')
		html.write('<tr><td colspan=2>')
		html.write(format(acc) + " total lines in assignment " + format(number-1))
		html.write('</td></tr>')
		html.write('</table>')
	html.write('</body>')
	html.write('</html>')
	html.close()
