#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-14.

Given: Three positive integers k, m, and n, representing a population 
containing k+m+n organisms: k individuals are homozygous dominant for
 a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms
 will produce an individual possessing a dominant allele (and thus
  displaying the dominant phenotype). Assume that any two organisms can mate.

"""

# we do this so that ints are automatically converted to floats for divison
from __future__ import division

import utils
import fileinput

def probability_recessive(k, m, n):
	pop = k + m + n
	homozygous_homozygous_matings = (n / pop) * ((n - 1) / (pop - 1))
	homozygous_heterozygous_matings = (n / pop) * (m / (pop - 1)) + (m / pop) * (n / (pop - 1))
	heterozygous_heterozygous_matings = (m / pop) * ((m - 1) / (pop - 1)) 
	import pdb; pdb.set_trace()
	probability_recessive = homozygous_homozygous_matings + .5 * homozygous_heterozygous_matings + .25 * heterozygous_heterozygous_matings
	return probability_recessive

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    k,m,n = args[0].split(' ')
    probability_dominant = 1 - probability_recessive(float(k), float(m), float(n))
    print probability_dominant

if __name__ == '__main__':
	main()