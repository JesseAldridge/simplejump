#!/usr/bin/python

import sys
import os

import utils

# Ignore special cd's.  Read and increment.  Write.

if sys.argv[-1] in ['..', '-']:
    sys.exit()

path_to_dir = utils.read_frecency_db()
target_path = os.path.abspath(os.path.join(*sys.argv[1:]))
path_to_dir[target_path].count += 1
path_to_dir[target_path].path = target_path

with open(utils.DB_PATH, 'w') as f:
    f.write('\n'.join([
        dir_.serialize() for path, dir_ in path_to_dir.items()]))
