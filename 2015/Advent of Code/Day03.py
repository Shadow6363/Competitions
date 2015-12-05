# -*- coding: utf-8 -*-

import sys


def main():
    directions = list(sys.stdin.readline())
    santa_coord_x, santa_coord_y = 0, 0
    robo_coord_x, robo_coord_y = 0, 0
    visited = { (santa_coord_x, santa_coord_y): True }

    for count, direction in enumerate(directions):
        if count % 2 == 0:
            if direction == '^':
                santa_coord_y += 1
            elif direction == 'v':
                santa_coord_y -= 1
            elif direction == '<':
                santa_coord_x -= 1
            else:
                santa_coord_x += 1

            visited[(santa_coord_x, santa_coord_y)] = True
        else:
            if direction == '^':
                robo_coord_y += 1
            elif direction == 'v':
                robo_coord_y -= 1
            elif direction == '<':
                robo_coord_x -= 1
            else:
                robo_coord_x += 1

            visited[(robo_coord_x, robo_coord_y)] = True

    print len(visited)

if __name__ == '__main__':
    main()
