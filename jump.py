#!/usr/bin/python

import sys
import os

import utils


def parse_args():
    path_num = sys.argv.pop()
    try:
        path_num = int(path_num)
    except ValueError:
        query = path_num
        path_num = 1
    else:
        query = sys.argv.pop()
    if query in ['..']:
        sys.exit()
    return query, path_num

def print_dir(query, path_num):
    # Print the most frecent dir matching the query.

    path_to_dir = utils.read_and_boost(query)

    count = 0
    for dir_ in sorted(
        path_to_dir.values(), key=lambda dir_: dir_.score, reverse=True):
        if os.path.isdir(dir_.path) and query.lower() in dir_.path.lower():
            count += 1
            if count == path_num:
                print dir_.path
                break
    else:
        print '.'

if len(sys.argv) == 1:
    print_dir('foo', 1)
else:
    print_dir(*parse_args())