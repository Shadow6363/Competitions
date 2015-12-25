# -*- coding: utf-8 -*-

import sys


class ChristmasComputer(object):
    def __init__(self, a=0, b=0):
        self.registers = {
            'a': a,
            'b': b,
            'pc': 0
        }

    def hlf(self, r):
        self.registers[r] /= 2
        self.registers['pc'] += 1

    def tpl(self, r):
        self.registers[r] *= 3
        self.registers['pc'] += 1

    def inc(self, r):
        self.registers[r] += 1
        self.registers['pc'] += 1

    def jmp(self, offset):
        offset = int(offset)
        self.registers['pc'] += offset

    def jie(self, r, offset):
        offset = int(offset)
        if self.registers[r] % 2 == 0:
            self.registers['pc'] += offset
        else:
            self.registers['pc'] += 1

    def jio(self, r, offset):
        offset = int(offset)
        if self.registers[r] == 1:
            self.registers['pc'] += offset
        else:
            self.registers['pc'] += 1


def main():
    instructions = [instruction.strip().split(' ', 1) for instruction in sys.stdin]
    computer = ChristmasComputer()

    instruction_map = {
        'hlf': computer.hlf,
        'tpl': computer.tpl,
        'inc': computer.inc,
        'jmp': computer.jmp,
        'jie': computer.jie,
        'jio': computer.jio
    }

    while computer.registers['pc'] < len(instructions):
        instruction, arg = instructions[computer.registers['pc']]
        instruction_map[instruction](*arg.split(', '))

    print computer.registers['b']


if __name__ == '__main__':
    main()
