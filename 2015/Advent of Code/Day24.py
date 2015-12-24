# -*- coding: utf-8 -*-

import collections
import itertools
import operator
import sys


def main():
    package_weights = [int(weight.strip()) for weight in sys.stdin]
    group_weight = sum(package_weights) / 3
    sum_dict = collections.defaultdict(list)
    combo_length = 1

    while group_weight not in sum_dict:
        for combo in itertools.combinations(package_weights, combo_length):
            sum_dict[sum(combo)].append(combo)
        combo_length += 1

    qe = min(reduce(operator.mul, group) for group in sum_dict[group_weight])

    print qe


if __name__ == '__main__':
    main()
