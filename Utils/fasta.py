#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2013-11-13.
"""

class fasta:
	def __init__(self, id):
		self.identifier = id
		self.content = ''

	def __str__(self):
		return self.identifier + ' ' + self.content

def parse(lines):
	fastas = []
	for line in lines:
		if len(line) > 0:
			if line[0] == '>':
				f = fasta(line[1:])
				fastas.append(f)
			else:
				fastas[-1].content += line
	return fastas

