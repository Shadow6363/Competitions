# -*- coding: utf-8 -*-

from collections import defaultdict

import itertools
import sys


distances = defaultdict(dict)

def tsp(start):
    costs = {}
    costs[(frozenset((start,)), start)] = 0

    for length in xrange(2, len(distances.keys()) + 1):
        combos = itertools.combinations(distances[start].keys(), length - 1)
        for vertices in combos:
            vertices_start = frozenset(vertices) | {start}

            costs[(vertices_start, start)] = float('-inf')

            for from_loc in vertices:
                costs[(vertices_start, from_loc)] = max(
                    costs[(vertices_start - {from_loc}, dest_loc)] +
                    distances[from_loc][dest_loc]
                    for dest_loc in vertices_start - {from_loc}
                )

    return max(
        costs[(frozenset(distances[start].keys()) | {start}, vertex)]
        for vertex in distances[start].keys()
    )

def main():
    for line in sys.stdin:
        line = line.strip()
        path, distance = line.split(' = ')
        from_loc, dest_loc = path.split(' to ')

        distances[from_loc][dest_loc] = int(distance)
        distances[dest_loc][from_loc] = int(distance)

    print max(tsp(start) for start in distances.iterkeys())


if __name__ == '__main__':
    main()
