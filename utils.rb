#!/usr/bin/ruby

require 'readline'

def protein_dict_from_file
	file = File.new("RNA_codon_table_1.txt", "r")
	protein_dict = {}
	while (line = file.gets)
		elems = line.split(' ')
		protein_dict[elems[0]] = elems[1]
	end
	file.close
	return protein_dict
end

def find_incidence(input, pattern)
	count = 0
	i = 0
	while(i + pattern.length <= input.length)
		if input[i, pattern.length] == pattern
			count += 1
		end
		i += 1
	end
	return count
end
