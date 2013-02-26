#!/usr/bin/python

import sys
import os

import utils

# Ignore special cd's.  Read and increment.  Write.

if sys.argv[-1] in ['..', '-']:
    sys.exit()

path_to_dir = utils.read_frecency_db()
# sys.argv ends with root dir and basename (because cd can be relative)
target_path = os.path.abspath(os.path.join(*sys.argv[1:]))
path_to_dir[target_path].count += 1
path_to_dir[target_path].path = target_path
path_to_dir[target_path].timestamp = time.time()

with open(utils.DB_PATH, 'w') as f:
    f.write('\n'.join([
        dir_.serialize() for path, dir_ in path_to_dir.items()]))