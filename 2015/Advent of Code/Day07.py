# -*- coding: utf-8 -*-

import operator
import sys


OPERATIONS = {
    'NOT': operator.invert,
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift
}

def main():
    instructions = {}

    for line in sys.stdin:
        lhs, rhs = [side.strip() for side in line.split('->')]
        lhs = lhs.split()

        try:
            lhs[0] = int(lhs[0])
        except ValueError:
            pass

        if len(lhs) == 1:
            instructions[rhs] = lhs[0]
        elif len(lhs) == 2:
            instructions[rhs] = (lhs[1], OPERATIONS[lhs[0]])
        elif len(lhs) == 3:
            try:
                lhs[2] = int(lhs[2])
            except ValueError:
                pass

            instructions[rhs] = (lhs[0], OPERATIONS[lhs[1]], lhs[2])

    instructions['b'] = 16076

    for wire, instruction in sorted(instructions.items(),
                                    key=lambda item: (len(item[0]), item[0])):
        if isinstance(instruction, (list, tuple)):
            if len(instruction) == 2:
                op = instruction[1]
                rhs = instructions[instruction[0]]
                instructions[wire] = op(rhs)
            elif len(instruction) == 3:
                op = instruction[1]

                if isinstance(instruction[0], (int, long)):
                    lhs = instruction[0]
                    rhs = instructions[instruction[2]]
                elif isinstance(instruction[2], (int, long)):
                    lhs = instructions[instruction[0]]
                    rhs = instruction[2]
                else:
                    lhs = instructions[instruction[0]]
                    rhs = instructions[instruction[2]]

                instructions[wire] = op(lhs, rhs)

    print instructions[instructions['a']]

if __name__ == '__main__':
    main()
