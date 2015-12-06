# -*- coding: utf-8 -*-

import re
import sys


def main():
    pair_two_regex = re.compile(r'([a-z][a-z])[a-z]*\1')
    dup_between_regex = re.compile(r'([a-z])[a-z]\1')
    nice = 0

    for line in sys.stdin:
        if pair_two_regex.search(line) and dup_between_regex.search(line):
            nice += 1

    print nice

if __name__ == '__main__':
    main()
