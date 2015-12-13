# -*- coding: utf-8 -*-

import collections
import itertools
import sys


def main():
    graph = collections.defaultdict(dict)

    for line in sys.stdin:
        line = line.strip().strip('.').split()
        person, _, sign, happy, _, _, _, _, _, _, other = line

        graph[person][other] = int(happy) if sign == 'gain' else -1*int(happy)

    max_happiness = float('-inf')

    for permutation in itertools.permutations(graph.iterkeys(), len(graph)):
        happiness = 0

        for person1, person2 in itertools.izip(permutation, permutation[1:]):
            happiness += graph[person1][person2]
            happiness += graph[person2][person1]
        happiness += graph[person2][permutation[0]]
        happiness += graph[permutation[0]][person2]

        max_happiness = max(max_happiness, happiness)

    print max_happiness

if __name__ == '__main__':
    main()
