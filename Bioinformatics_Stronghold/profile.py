#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-14.

Profile Matrix

"""

BASES = ('A','C','T','G')

def profile_matrix(fastas):

	# profile is an array of base count dictionaries initialized to zero
	profile = []
	for i in range(len(fastas[0].content)):
		d = {}
		for b in BASES:
			d[b] = 0
		profile.append(d)
	for fasta in fastas:
		i = 0
		for base in fasta.content:
			profile[i][base] += 1
			i += 1
	return profile

def pretty_print(profile_matrix):
	for b in BASES:
		row = b + ':'
		for bases_count in profile_matrix:
			row += ' '  + str(bases_count[b])
		print row