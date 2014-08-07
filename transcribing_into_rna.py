#!/usr/bin/env python
# encoding: utf-8
"""

Created by Nick DeVeaux on 2014-08-07.

"""

import fileinput

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    input = args[0]
    print(input.replace('T', 'U'))

if __name__ == '__main__':
	main()