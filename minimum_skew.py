#!/usr/bin/env python
# encoding: utf-8
"""
minimum_skew.py

Created by Nick DeVeaux on 2013-11-14.
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
    import pdb; pdb.set_trace()
    utils.print_array(skew_array)

def iterative_skew(input):
    base_counts = {'C':0, 'G':0, 'A':0, 'T':0}
    ratio = {}
    i = 0
    for char in input:
        base_counts[char] += 1
        ratio[base_counts['G']-base_counts['C']] = i
        i += 1
    return ratio[min(ratio)]

if __name__ == '__main__':
    main()

