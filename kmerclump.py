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

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    input = args[0]
    k = args[1]
    L = args[2]
    t = args[3]
    kmers = find_clumps(input, k, L, t);
    utils.print_array(kmers)
    
def find_clumps(input, k, L, t):
    importpdb;


if __name__ == '__main__':
	main()

