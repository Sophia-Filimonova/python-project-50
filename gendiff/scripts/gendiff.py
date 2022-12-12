#!/usr/bin/env python3

from gendiff import generate_diff, input_args


def main():

    args = input_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
