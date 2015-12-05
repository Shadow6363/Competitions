# -*- coding: utf-8 -*-

import sys


def main():
    instructions = sys.stdin.readline()
    floor = 0

    for num, instruction in enumerate(instructions):
        if instruction == '(':
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            print num + 1
            break

if __name__ == '__main__':
    main()
