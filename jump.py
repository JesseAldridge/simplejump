#!/usr/bin/python

import sys
import os

import utils

if 'SIMPLE_JUMP_CD' not in os.environ:
    sys.stderr.write('Something stole cd!\n')
    sys.stderr.write(os.system('type cd'))

def print_dir(query):

    # Print the most frecent dir matching the query.

    path_to_dir = utils.read_and_boost(query)
    paths = sorted(
        path_to_dir.values(), key=lambda dir_: dir_.score, reverse=True)
    count = 0
    for dir_ in paths:
        if os.path.isdir(dir_.path) and query.lower() in dir_.path.lower():
            print dir_.path
            break
    else:
        print '.'

if len(sys.argv) == 1:
    print_dir('foo', 1)
else:
    query = sys.argv.pop()
    if query in ['..']:
        sys.exit()
    print_dir(query)
