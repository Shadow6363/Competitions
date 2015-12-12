# -*- coding: utf-8 -*-

import re
import sys


def main():
    start_num = sys.stdin.readline().strip()

    num_regex = re.compile(r'([0-9])\1*')

    for _ in xrange(50):
        result = []
        index = 0
        match = num_regex.search(start_num, index)

        while match:
            result.append('{0}{1}'.format(match.end() - index, match.group(0)[0]))
            index = match.end()
            match = num_regex.search(start_num, index)

        start_num = ''.join(result)

    print len(start_num)


if __name__ == '__main__':
    main()
