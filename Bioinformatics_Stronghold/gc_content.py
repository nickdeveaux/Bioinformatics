#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-07.

Problem

The GC-content of a DNA string is given by the percentage of symbols in the 
string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%.
 Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database.
 A commonly used method of string labeling is called FASTA format. 
 In this format, the string is introduced by a line that begins with '>', 
 followed by some labeling information. Subsequent lines contain the string itself;
  the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the
 ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
 GC-content of that string. Rosalind allows for a default error of 0.001 in 
 all decimal answers unless otherwise stated; please see the note on absolute
  error below.

"""

# we do this so that ints are automatically converted to floats for divison
from __future__ import division

import fileinput
import utils
import fasta

def gc_content(fastas):
	gc_content = {}
	for fasta in fastas:
		gc_count = 0
		for base in fasta.content:
			if base in ('G', 'C'):
				gc_count += 1
		gc_content[fasta.identifier] = gc_count / len(fasta.content)
	return gc_content


def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    fastas = fasta.parse(args)
    
    # get the highest gc percentage fasta and print it pretty as a percentage
    sorted_gc = sorted(gc_content(fastas).items(), key=lambda t: -t[1])
    print sorted_gc[0][0] + ' ' + str(sorted_gc[0][1] * 100)

if __name__ == '__main__':
	main()