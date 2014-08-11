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

# dynamic programming approach: store all the values at time t
def mortal_rabbits(n, m):
	rabbits = []
	born_rabbits = []
	rabbits.insert(0, 0)
	rabbits.insert(1, 1)
	born_rabbits.insert(0, 0) # need to store index 0
	born_rabbits.insert(1, 1) # need to store index 1
	t = 1
	while (t < n):
		t += 1
		dead = 0
		if t-m > 0:
			dead = born_rabbits[t-m] + born_rabbits[t-m - 1]
		i = rabbits[t-1] + rabbits[t-2] - dead

		# born (at time t) = diff from the last time, plus the number of dead
		born_rabbits.insert(t, i - rabbits[t-1] + dead)
		rabbits.insert(t, i)
	return rabbits[n]
	

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    n,m = args[0].split(' ')
    print mortal_rabbits(int(n), int(m))

if __name__ == '__main__':
	main()