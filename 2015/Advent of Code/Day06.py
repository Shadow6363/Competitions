# -*- coding: utf-8 -*-

import sys


def main():
    grid = [[False for _ in xrange(1000)] for _ in xrange(1000)]
    lit = 0

    for line in sys.stdin:
        instruction, from_coords, _, dest_coords = line.strip().rsplit(' ', 3)
        from_coords = [int(coord) for coord in from_coords.split(',')]
        dest_coords = [int(coord) for coord in dest_coords.split(',')]

        for x_coord in xrange(from_coords[0], dest_coords[0] + 1):
            for y_coord in xrange(from_coords[1], dest_coords[1] + 1):
                if instruction == 'turn on':
                    if not grid[x_coord][y_coord]:
                        grid[x_coord][y_coord] = True
                        lit += 1
                elif instruction == 'turn off':
                    if grid[x_coord][y_coord]:
                        grid[x_coord][y_coord] = False
                        lit -= 1
                else:
                    if grid[x_coord][y_coord]:
                        grid[x_coord][y_coord] = False
                        lit -= 1
                    else:
                        grid[x_coord][y_coord] = True
                        lit += 1

    print lit

if __name__ == '__main__':
    main()
