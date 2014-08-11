#!/usr/bin/ruby

require 'readline'

$codon_amino_acid_encoding_file = "../Data/RNA_codon_table_1.txt"

def string_from_file(filename)
	file = File.open(filename, "rb")
	output = file.read
	file.close
	return output
end

def codon_to_peptide_dict
	file = File.new($codon_amino_acid_encoding_file, "r")
	protein_dict = {}
	while (line = file.gets)
		elems = line.split(' ')
		protein_dict[elems[0]] = elems[1]
	end
	file.close
	return protein_dict
end

def peptide_to_codon_dict
	file = File.new($codon_amino_acid_encoding_file, "r")
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
	indices = []
	while(i + pattern.length <= input.length)
		if input[i, pattern.length] == pattern
			count += 1
			indices.push(i)
		end
		i += 1
	end
	return count, indices
end

def reverse_complement(input)
    input = input.downcase
    genome = {'a' => 't', 'c' =>'g','t'=>'a', 'g'=>'c'}
    output = ''
    input.reverse.each_char do |c|
        output += genome[c]
    end
    return output.upcase!
end
