#!/usr/bin/python

import sys
import os
import time

import utils

# Ignore special cd's.  Read and increment.  Write.

if sys.argv[-1] in ['..', '-']:
    sys.exit()

path_to_dir = utils.read_frecency_db()
# sys.argv: [<this script>, <cwd>, <target>];  get the full path
target_path = os.path.abspath(os.path.join(*sys.argv[1:]))
if target_path not in path_to_dir:
    path_to_dir[target_path] = utils.Dir()
path_to_dir[target_path].count += 1
path_to_dir[target_path].path = target_path
path_to_dir[target_path].timestamp = time.time()

f = open(utils.DB_PATH, 'w')
try:
    f.write('\n'.join([
            dir_.serialize() for path, dir_ in path_to_dir.items()]))
finally:
    f.close()
