# -*- coding: utf-8 -*-

import re
import sys


def main():
    vowel_regex = re.compile(r'[aeiou][^aeiou]*[aeiou][^aeiou]*[aeiou]')
    dup_regex = re.compile(r'([a-z])\1')
    nice = 0

    for line in sys.stdin:
        if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
            continue
        if vowel_regex.search(line) and dup_regex.search(line):
            nice += 1

    print nice

if __name__ == '__main__':
    main()
