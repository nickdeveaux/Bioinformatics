#!/usr/bin/ruby

require 'readline'

def codon_to_peptide_dict
	file = File.new("RNA_codon_table_1.txt", "r")
	protein_dict = {}
	while (line = file.gets)
		elems = line.split(' ')
		protein_dict[elems[0]] = elems[1]
	end
	file.close
	return protein_dict
end

def peptide_to_codon_dict
	file = File.new("RNA_codon_table_1.txt", "r")
	protein_dict = {}
	while (line = file.gets)
		elems = line.split(' ')
		if protein_dict[elems[1]]
			protein_dict[elems[1]] = protein_dict[elems[1]].push(elems[0])
		else
			protein_dict[elems[1]] = [elems[0]]
		end
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
