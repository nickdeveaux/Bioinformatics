#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-14.

Consensus String

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible 
	consensus strings exist, then you may return any one of them.)

"""

import fileinput
import utils
import fasta
import profile

def consensus_string(profile):
	consensus_string = ''
	for base_counts in profile:
		sorted_bases_by_most_common_first = sorted(base_counts.items(), key=lambda t: -t[1])
		consensus_string += sorted_bases_by_most_common_first[0][0]
	return consensus_string

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    fastas = fasta.parse(args)
    profile_matrix = profile.profile_matrix(fastas)
    print consensus_string(profile_matrix)
    profile.pretty_print(profile_matrix)

if __name__ == '__main__':
	main()