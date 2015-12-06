# -*- coding: utf-8 -*-

import sys


def main():
    grid = [[0 for _ in xrange(1000)] for _ in xrange(1000)]
    brightness = 0

    for line in sys.stdin:
        instruction, from_coords, _, dest_coords = line.strip().rsplit(' ', 3)
        from_coords = [int(coord) for coord in from_coords.split(',')]
        dest_coords = [int(coord) for coord in dest_coords.split(',')]

        for x_coord in xrange(from_coords[0], dest_coords[0] + 1):
            for y_coord in xrange(from_coords[1], dest_coords[1] + 1):
                if instruction == 'turn on':
                    brightness += 1
                    grid[x_coord][y_coord] += 1
                elif instruction == 'turn off':
                    if grid[x_coord][y_coord] > 0:
                        brightness -= 1
                        grid[x_coord][y_coord] -= 1
                else:
                    brightness += 2
                    grid[x_coord][y_coord] += 2

    print brightness

if __name__ == '__main__':
    main()
