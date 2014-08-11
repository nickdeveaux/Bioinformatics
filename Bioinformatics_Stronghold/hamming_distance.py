#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-07.

Given two strings s and t of equal length, the Hamming distance between s and t,
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

"""

import utils
import fileinput

def hamming_distance(a, b):
	distance = 0
	for i in range (len(a)):
		if a[i] != b[i]:
			distance += 1
	return distance


def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    a = args[0]
    b = args[1]
    print(hamming_distance(a, b))

if __name__ == '__main__':
	main()