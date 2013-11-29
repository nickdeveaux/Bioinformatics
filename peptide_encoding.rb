
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
peptide = ARGV[1]
pep_dict =  peptide_to_codon_dict

possible_translations = []
peptide.each_char { |amino_acid|
    temp =  possible_translations
    possible_translations = []
    if temp.empty?
    	pep_dict[amino_acid].each{ |comb|
	    	possible_translations << comb
	    }
    else
	temp.each { |string|
	    pep_dict[amino_acid].each{ |comb|
	    	possible_translations << string + comb
	    }
	}
	end
}
possible_translations.each { |pattern|
    pattern.gsub!("U", "T")
    [pattern, reverse_complement(pattern)].each{ |p| 
		count, indices = find_incidence(inp, p)
		if count > 0
			indices.each {
				puts p
			}
		end
	}
}

