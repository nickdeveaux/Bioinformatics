#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-07.

"""

import fileinput
import utils
import fasta

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    print(fasta.parse(args))

if __name__ == '__main__':
	main()