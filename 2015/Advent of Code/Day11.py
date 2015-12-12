# -*- coding: utf-8 -*-

import itertools
import re
import sys


def letters_sorted(password):
    x_it, y_it, z_it = iter(password), iter(password[1:]), iter(password[2:])

    return any(
        ord(x) == ord(y) - 1 and ord(y) == ord(z) - 1
        for x, y, z in itertools.izip(x_it, y_it, z_it)
    )

def two_pair(password):
    pair = re.compile(r'([a-z])\1')
    match1_iter, match2_iter = pair.finditer(password), pair.finditer(password)

    try:
        next(match2_iter)

        return any(
            match1.group(0) != match2.group(0)
            for match1, match2 in itertools.izip(match1_iter, match2_iter)
        )
    except StopIteration:
        return False

def increment(password):
    new_password = []
    carry = True

    for letter in reversed(password):
        if carry:
            if letter == 'z':
                new_password.append('a')
            else:
                if letter in ('h', 'k', 'n'):
                    new_password.append(chr(ord(letter) + 2))
                else:
                    new_password.append(chr(ord(letter) + 1))
                carry = False
        else:
            new_password.append(letter)
    return ''.join(reversed(new_password))

def main():
    curr_pass = sys.stdin.readline().strip()
    new_password = increment(curr_pass)

    while True:
        if letters_sorted(new_password) and two_pair(new_password):
            break
        else:
            new_password = increment(new_password)

    new_password = increment(new_password)

    while True:
        if letters_sorted(new_password) and two_pair(new_password):
            break
        else:
            new_password = increment(new_password)

    print new_password


if __name__ == '__main__':
    main()
