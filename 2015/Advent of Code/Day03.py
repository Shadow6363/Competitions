# -*- coding: utf-8 -*-

import sys


def main():
    directions = list(sys.stdin.readline())
    coord_x, coord_y = 0, 0
    visited = { (coord_x, coord_y): True }

    for direction in directions:
        if direction == '^':
            coord_y += 1
        elif direction == 'v':
            coord_y -= 1
        elif direction == '<':
            coord_x -= 1
        else:
            coord_x += 1

        visited[(coord_x, coord_y)] = True

    print len(visited)

if __name__ == '__main__':
    main()
