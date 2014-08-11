#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-07.

Rabbits and Recurrence Relations

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

Assumption: A pair of rabbits only produce a new pair of offspring every month

"""

import utils
import fileinput

def mortal_rabbits(n, m):
	rabbits = []
	rabbits[0] = 0
	rabbits[1] = 1
	t = 1
	while (t < n):
		i = rabbits[t-1] + rabbits[t-2]
		if t-m > 0:
			i -= rabbits[t-m]
		rabbits[t] = i
		t += 1
	return rabbits[t]
	

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    n,m = args[0].split(' ')
    print mortal_rabbits(int(n), int(m))

if __name__ == '__main__':
	main()