# -*- coding: utf-8 -*-

import json
import re
import sys


def filter_red(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if value == 'red':
                return None
            elif isinstance(value, (dict,list)):
                obj[key] = filter_red(value)
    elif isinstance(obj, list):
        for idx, value in enumerate(obj):
            if isinstance(value, (dict,list)):
                obj[idx] = filter_red(value)
    return obj

def main():
    document = sys.stdin.readline().strip()
    num_regex = re.compile(r'(\-?\d+)')

    document = json.loads(document)
    filter_red(document)
    document = json.dumps(document)

    print sum(
        int(num_match.group(0)) for num_match in num_regex.finditer(document)
    )


if __name__ == '__main__':
    main()
