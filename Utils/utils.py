#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

Created by Nick DeVeaux on 2013-11-13.
"""

def print_array(array):
    output = ''
    for a in array:
        output += str(a) + ' '
    print output

def reverse_dna(input):
    input = input.lower()
    genome = {'a':'t', 'c':'g','t':'a', 'g':'c'}
    output = ''
    for c in input[::-1]:
        output += genome[c]
    return output.upper()