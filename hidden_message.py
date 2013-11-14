#!/usr/bin/env python
# encoding: utf-8
"""
hidden_message.py

Created by Nick DeVeaux on 2013-11-08.

"""

import sys
import os
from sets import Set

def find_most_common_substring(input):
    most_common_string = []
    most_common_count = 0
    for i in range(1, len(input)):
        pattern, count = find_most_common_kmer(input, i)
        if count > most_common_count:
            most_common_count = count
            most_common_strings=Set([pattern])
        if count == most_common_count:
            most_common_strings.update([pattern])
    return most_common_strings,  most_common_count 

def find_most_common_kmer(input, k):
    most_common_strings = Set([])
    most_common_count = 0
    for i in range(0, len(input)-k):
        pattern = input[i:i+k]
        count, indices = find_incidence(input, pattern)
        if count > most_common_count:
            most_common_count = count
            most_common_strings=Set([pattern])
        if count == most_common_count:
            most_common_strings.update([pattern])
    return most_common_strings,  most_common_count 

def find_incidence(input, pattern):
    i = 0
    count = 0
    indices = []
    ##import pdb; pdb.set_trace()
    while ( i + len(pattern) <= len(input)):
        if input[i:i+len(pattern)] == pattern:
            indices.append(i)
            count += 1
        i += 1
    return count, indices
    
def reverse_dna(input):
    input = input.lower()
    genome = {'a':'t', 'c':'g','t':'a', 'g':'c'}
    output = ''
    for c in input[::-1]:
        output += genome[c]
    return output.upper()

def main():
    input = sys.argv[1]
    pattern = sys.argv[2]
    count, indices = find_incidence(input, pattern);
    print indices(input, pattern)
    
def hidden_message():
    import fileinput
    for line in fileinput.input():
        print line
    if len(sys.argv) > 3:
        print 'Expected usage: hidden_message.py <input> <optional-n>'
        exit()
    input = sys.argv[1]
    if len(sys.argv) == 3:
        k= int(sys.argv[2])
        print input
        print k
        most_common_strings, count= find_most_common_kmer(input, k)
        output = ''
        for s in most_common_strings:
            output += s + ' '
        print output
    if len(sys.argv)==2:
        print find_most_common_substring(input)

if __name__ == '__main__':
	main()

