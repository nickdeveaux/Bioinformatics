
import sys
import os
import utils
import fileinput

def nucleiotide_incidence(seq):
	incidence = []
	for bp in ('A', 'C', 'G', 'T'):
		incidence.append(seq.count(bp))
	return incidence


def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    input = args[0]
    utils.print_array(nucleiotide_incidence(input))

if __name__ == '__main__':
	main()