#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  

import os
import dir_walker
import makehtml
import process
import jmail

global path

def main():
	os.chdir(os.pardir)
	path = os.getcwd()
	assignments = dir_walker.take_a_walk()
	makehtml.write(assignments)
	process.makezip(assignments[1])
	email = input("Enter email: ")
	jmail.send(email)
	return 0

if __name__ == '__main__':
	main()

