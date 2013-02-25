#!/usr/bin/python

import sys
import os
import logging

import utils

# ----------

# sys.argv: ['.../on_cd.py', pwd, target_dir]

# db format
# <count> <time> <path>
# 2 1358624598.17 ~/foo/bar
# 1 1358624611.5 ~/foo/bar/baz

# ----------

# Print the most frecent dir matching the query.

def main():
    # logging.info('sys.argv: {0}'.format(sys.argv))

    query = sys.argv[-1]
    if query in ['..']:
        sys.exit()

    path_to_dir = utils.read_and_boost(query)

    for dir_ in sorted(
        path_to_dir.values(), key=lambda dir_: dir_.score, reverse=True):
        if os.path.isdir(dir_.path):
            print dir_.path
            return True

if __name__ == '__main__':
    main()