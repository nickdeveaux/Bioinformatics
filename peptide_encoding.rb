
"""
peptide_encoding.rb

Created by Nick DeVeaux on 2013-11-24.

Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
     Input: A DNA string Text and an amino acid string Peptide.
     Output: All substrings of Text encoding Peptide (if any such substrings exist).
"""

#!/usr/bin/ruby

require_relative 'utils'

inp = ARGV[0]
pattern = ARGV[1]
print peptide_to_codon_dict

