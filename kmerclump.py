#!/usr/bin/env python
# encoding: utf-8
"""
kmerclump.py

Created by Nick DeVeaux on 2013-11-13.

Clump Finding Problem: Find patterns forming clumps in a string.
     Input: A string Genome, and integers k, L, and t.
     Output: All distinct k-mers forming (L, t)-clumps in Genome.
"""

import sys
import os
import utils
import fileinput
from sets import Set

def main():
    args = []
    for line in fileinput.input():
        elems = line.rstrip().split(' ')
        for el in elems:
            if el != 'Input':
                args.append(el)
    input = args[0]
    k = int(args[1])
    L = int(args[2])
    t = int(args[3])
    kmers = find_clumps(input, k, L, t);
    utils.print_array(kmers)

# create a dictionary of all locations of all kmers in input
def find_clumps(input, k, L, t):
    i = 0
    kmer_locations = {}
    kmer_clumps = Set([])
    while ( i + k <= len(input)):
        kmer = input[i:i+k] 
        if kmer_locations.has_key(kmer):
            kmer_locations[kmer].append(i)
            if is_clump(kmer_locations[kmer], L, t, i):
                kmer_clumps.add(kmer)
        else:
            kmer_locations[kmer]=[i]
        i += 1
    return kmer_clumps

# Are there t or more distinct kmers within distance L of i?
def is_clump(kmer_indices, L, t, i):
    count = 0
    for index in kmer_indices:
        if i - index <= L:
            count += 1
    if count >= t:
        return True
    else:
        return False
            

if __name__ == '__main__':
	main()

