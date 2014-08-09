#!/usr/bin/env python
# encoding: utf-8
"""
minimum_skew.py

Created by Nick DeVeaux on 2013-11-14.

Minimum Skew Problem: Find a position in a genome minimizing the skew.
     Input: A DNA string Genome.
     Output: All integer(s) i minimizing Skew(Prefixi (Text)) among all values of i (from 0 to |Genome|).
"""

import sys
import os
import fileinput
import utils

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    input = args[0]
    skew_array = iterative_skew(input)
    utils.print_array(skew_array)

def iterative_skew(input):
    base_counts = {'C':0, 'G':0, 'A':0, 'T':0}
    ratio = {0:[0]}
    i = 1
    for char in input:
        base_counts[char] += 1
        diff = base_counts['G']-base_counts['C']
        if ratio.has_key(diff):
            ratio[diff].append(i)
        else:
            ratio[diff] = [i]
        i += 1
    return ratio[min(ratio)]

if __name__ == '__main__':
    main()

