# -*- coding: utf-8 -*-

import hashlib
import sys


def main():
    key = sys.stdin.readline().strip()
    key_hash = hashlib.md5()
    key_hash.update(key)

    for num in xrange(100000000000):
        guess_hash = key_hash.copy()
        guess_hash.update(str(num))

        if guess_hash.hexdigest().startswith('00000'):
            print num
            break

if __name__ == '__main__':
    main()
