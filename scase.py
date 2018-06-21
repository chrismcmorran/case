#!/usr/local/bin/python3

import argparse
import sys


def create_parser():
    if len(sys.argv) <= 1:
        sys.argv.append('-h')
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--upper", "-u", help="Convert to upper case.", action='store_true')
    parser.add_argument(
        "--lower", "-l", help="Convert to lower case.", action='store_true')
    parser.add_argument(
        "--proper", "-p", help="Convert to proper case.", action='store_true')
    parser.add_argument(
        "--string", "-s", help="The string to convert.")
    return parser.parse_args()


def main():
    args = create_parser()
    string = args.string

    try: 
        if args.upper:
            print(string.upper())

        if args.lower:
            print(string.lower())

        if args.proper:
            print(string.capitalize())
    except (BrokenPipeError, IOError):
        print ('BrokenPipeError caught', file = sys.stderr)


main()
