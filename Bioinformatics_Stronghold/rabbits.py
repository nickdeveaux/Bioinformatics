#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-07.

Rabbits and Recurrence Relations

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, 
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

"""

import utils
import fileinput

def fibonacci(n, k):
	if n == 1:
		return 1
	if n == 0:
		return 0
	return fibonacci(n-1, k) + k * fibonacci(n-2, k)

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    n,k = args[0].split(' ')
    print fibonacci(int(n), int(k))

if __name__ == '__main__':
	main()