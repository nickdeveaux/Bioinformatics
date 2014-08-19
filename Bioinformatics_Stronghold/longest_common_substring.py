#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-07.

Problem:

A common substring of a collection of strings is a substring of every member of the collection.
 We say that a common substring is a longest common substring if there does not exist a longer 
 common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGGTATA",
  but it is not as long as possible; in this case, "GTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" 
are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any 
	single solution.)


"""

import fasta
from sets import Set
import fileinput

MINIMUM_CHARS = 1

def get_common_substrings(a, b):
	common_substrings = Set()
	match_length_matrix = {}
	for i in range(len(a)):
		current_match = ''
		# hold on to the temporary index increment from the comparer char	
		cursor = 0   
		for j in range(len(b)):
			match_length_matrix[(i,j)] = 0
			if (cursor + i >= len(a)):
				break
			x = a[i + cursor]
			y = b[j]
			if x == y:
				current_match += y
				cursor += 1
			else:
				# don't bother storing common substrings with X chars
				if len(current_match) > MINIMUM_CHARS:
					if i ==0 or j-cursor == 0 or len(current_match) >= match_length_matrix[(i-1, j-1-cursor)]:
						common_substrings.add(current_match)
					match_length_matrix[(i,j-cursor)] = len(current_match)
					current_match = ''
					cursor = 0
		if len(current_match) > MINIMUM_CHARS:
			if i ==0 or j-cursor == 0 or len(current_match) >= match_length_matrix[(i-1, j-1-cursor)]:
				common_substrings.add(current_match)
			match_length_matrix[(i,j-cursor)] = len(current_match)
	print match_length_matrix
	print common_substrings
	return common_substrings

def filter_out_substrings(next_common_substrings):
    	common_substrings = Set()
    	for a in next_common_substrings:
    		is_prefix = False
    		for b in next_common_substrings:
    			if b != a:
    				if b.startswith(a):
    					is_prefix = True
    					break
    		if not is_prefix:
    			common_substrings.add(a)
    	return common_substrings

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    fastas = fasta.parse(args)
    common_substrings = Set([fastas[0].content])

    # iterate through fastas, compiling and updating a set of common substrings
    for f in fastas[1:]:
    	next_common_substrings = Set()
    	for s in common_substrings:
    		next_common_substrings.update(get_common_substrings(f.content, s))

    	common_substrings = next_common_substrings

    sorted_common_substrings = sorted(common_substrings, key=lambda t: -len(t))
    print sorted_common_substrings[0]

if __name__ == '__main__':
	main()
