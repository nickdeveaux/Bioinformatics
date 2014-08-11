#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

Created by Nick DeVeaux on 2013-11-13.
"""

codon_amino_acid_encoding_file = "../Data/RNA_codon_table_1.txt"

def codon_to_peptide_dict():
    file = open(codon_amino_acid_encoding_file, "r")
    protein_dict = []
    for line in file:
        elems = line.split(' ')
        protein_dict[elems[0]] = elems[1]
    file.close()
    return protein_dict

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