#!/usr/bin/ruby

require_relative 'utils'

inp = ARGV[0]
protein_dict = codon_to_peptide_dict

codons = inp.scan(/.{3}/)
result = ""
codons.each{ |c| 
	if protein_dict[c]!= nil
	    result += protein_dict[c]
	end
}
print result


