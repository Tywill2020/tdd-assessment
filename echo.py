#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = 'Tyrell Williams with help from Dan'


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parse = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parse.add_argument('text', help='text to be manipulated')
    parse.add_argument('-u', '--upper', action='store_true',
                       help="convert text to uppercase")
    parse.add_argument('-l', '--lower', action='store_true',
                       help="convert text to lowercase")
    parse.add_argument('-t', '--title', action='store_true',
                       help="convert text to titlecase")
    return parse


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)
    msg = args.text
    if args.upper:
        msg = msg.upper()
    if args.lower:
        msg = msg.lower()
    if args.title:
        msg = msg.title()

    print(msg)


if __name__ == '__main__':
    main(sys.argv[1:])
