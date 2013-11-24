#!/usr/bin/ruby

require_relative 'utils'

inp = ARGV[0]
puts inp
protein_dict = protein_dict_from_file

codons = inp.scan(/.{3}/)
result = ""
codons.each{ |c| 
	if protein_dict[c]!= nil
	    result += protein_dict[c]
	end
}
print result


