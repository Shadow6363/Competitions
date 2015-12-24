# -*- coding: utf-8 -*-

import math
import sys


# Courtesy of http://stackoverflow.com/a/6800214
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))

def presents_delivered_by(elves):
    return sum(elf*10 for elf in elves)

def main():
    min_presents = int(sys.stdin.readline().strip())
    house_num, presents = 1000, 0

    while presents < min_presents:
        house_num += 1
        presents = presents_delivered_by(
            factors(house_num)
        )

    print house_num


if __name__ == '__main__':
    main()
