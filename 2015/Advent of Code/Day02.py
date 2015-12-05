# -*- coding: utf-8 -*-

import sys


def main():
    dimensions = []
    sq_ft_paper, ft_ribbon = 0, 0

    for line in sys.stdin:
        dimensions.append(sorted([int(dimension) for dimension in line.split('x')]))

    for dimension in dimensions:
        sq_ft_paper += 3 * (dimension[0] * dimension[1])
        sq_ft_paper += 2 * (dimension[0] * dimension[2])
        sq_ft_paper += 2 * (dimension[1] * dimension[2])

        ft_ribbon += (dimension[0] * dimension[1] * dimension[2])
        ft_ribbon += (2 * dimension[0]) + (2 * dimension[1])

    print ft_ribbon

if __name__ == '__main__':
    main()
