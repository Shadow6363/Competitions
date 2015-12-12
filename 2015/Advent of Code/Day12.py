# -*- coding: utf-8 -*-

import re
import sys


def main():
    document = sys.stdin.readline().strip()
    num_regex = re.compile(r'(\-?\d+)')

    print sum(
        int(num_match.group(0)) for num_match in num_regex.finditer(document)
    )


if __name__ == '__main__':
    main()
