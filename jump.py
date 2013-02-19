#!/usr/bin/python

import sys
import os
import logging

import lib

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

    if sys.argv[-1] in ['..']:
        sys.exit()

    path_to_dir = lib.read_frecency_db()

    def jump(path_transform):
        for _, dir_ in sorted(
            path_to_dir.items(), key=lambda t: t[-1].frecency, reverse=True):
            if sys.argv[-1].lower() in path_transform(dir_.path).lower():
                if os.path.exists(dir_.path):
                    print dir_.path
                    return True

    for transform in [lambda path: os.path.basename(path), lambda path: path]:
        if jump(transform):
            return

if __name__ == '__main__':
    main()