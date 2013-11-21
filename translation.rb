#!/usr/bin/ruby

require 'readline'

inp = ARGV[0]
puts inp
file = File.new("RNA_codon_table_1.txt", "r")
protein_dict = {}
while (line = file.gets)
	elems = line.split(' ')
	protein_dict[elems[0]] = elems[1]
end
file.close

codons = inp.scan(/.{3}/)
result = ""
codons.each{ |c| 
	if protein_dict[c]!= nil
	    result += protein_dict[c]
	end
}
print result


