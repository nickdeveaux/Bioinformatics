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

Runtime: creates the hash set of all possible substrings in n squared, n being the length of one of the inputs 
Hash lookups take constant time, so intersections across sets of length n squared take n squared in time. 
Average time: n^2 * m , where n is the average size of an input, and m is the number of inputs. 

"""

import fasta
from sets import Set
import fileinput

def permutation_set(string):
	permutations = Set()
	for i in range(len(string) -1):
		for j in range(len(string) - i ):
			permutations.add(string[i: i + j + 1])
	return permutations

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    fastas = fasta.parse(args)
    strings = []
    for f in fastas:
    	strings.append(f.content)
    first = strings[0]
    intersect_set = permutation_set(first)
    for s in strings[1:]:
    	intersect_set = intersect_set & permutation_set(s)
    print max(intersect_set, key=len)

if __name__ == '__main__':
	main()
