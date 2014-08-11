#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2013-11-13.
"""

def fasta():
	identifier = ''

def parse(lines):
	fastas = []
	for line in lines:
		if len(line) > 0:
			if line[0] == '>':
				f = fasta()
				f.identifier = line[1:]
				f.content = ''
				fastas.append(f)
			else:
				f.content += line
	return fastas

