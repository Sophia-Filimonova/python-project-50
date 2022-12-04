#!/usr/bin/env python3

import argparse
from gendiff import generate_diff
from gendiff.formaters import stylish
from gendiff.formaters import plain
from gendiff.formaters import to_json


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='stylish',
        help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()

    if args.format == 'stylish':
        diff = generate_diff(args.first_file, args.second_file, stylish)
    elif args.format == 'plain':
        diff = generate_diff(args.first_file, args.second_file, plain)
    elif args.format == 'json':
        diff = generate_diff(args.first_file, args.second_file, to_json)

    print(diff)


if __name__ == '__main__':
    main()
