# -*- coding: utf-8 -*-

import ast
import sys


def main():
    num_char_code, num_char_mem = 0, 0

    for line in sys.stdin:
        line = line.strip()
        num_char_code += len(line)

        eval_line = ast.literal_eval(line)
        num_char_mem += len(eval_line)

    print num_char_code - num_char_mem

if __name__ == '__main__':
    main()
