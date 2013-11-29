
"""
peptide_encoding.rb

Created by Nick DeVeaux on 2013-11-24.

Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
     Input: A DNA string Text and an amino acid string Peptide.
     Output: All substrings of Text encoding Peptide (if any such substrings exist).
"""

#!/usr/bin/ruby

require_relative 'utils'

def all_possible_dna_translations(peptide)
	possible_translations = []
	pep_dict =  peptide_to_codon_dict
	peptide.each_char { |amino_acid|
	    temp =  possible_translations
	    possible_translations = []
	    if temp.empty?
	    	pep_dict[amino_acid].each{ |combo|
		    	possible_translations << combo
		    }
	    else
		temp.each { |string|
		    pep_dict[amino_acid].each{ |combo|
		    	possible_translations << string + combo
		    }
		}
		end
	}
	return possible_translations
end

def all_incidences_of_pattern_in_dna(dna, patterns)
	output = []
	patterns.each { |pattern|
	    pattern.gsub!("U", "T")
	    [pattern, reverse_complement(pattern)].each{ |p| 
			count, indices = find_incidence(dna, p)
			if count > 0
				indices.each {
					output << p
				}
			end
		}
	}
	return output
end

# main
dna = ARGV[0]
peptide = ARGV[1]
translations = all_possible_dna_translations(peptide)
puts all_incidences_of_pattern_in_dna(dna, translations)