# -*- coding: utf-8 -*-

import sys


def main():
    dimensions = []
    sq_ft = 0

    for line in sys.stdin:
        dimensions.append(sorted([int(dimension) for dimension in line.split('x')]))

    for dimension in dimensions:
        sq_ft += 3 * (dimension[0] * dimension[1])
        sq_ft += 2 * (dimension[0] * dimension[2])
        sq_ft += 2 * (dimension[1] * dimension[2])

    print sq_ft

if __name__ == '__main__':
    main()
