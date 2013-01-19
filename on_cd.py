#!/usr/bin/python

import sys
import os

import lib

# ----------

# sys.argv: ['.../on_cd.py', pwd, target_dir]

# db format
# <count> <time> <path>
# 2 1358624598.17 ~/foo/bar
# 1 1358624611.5 ~/foo/bar/baz

# ----------

if sys.argv[-1] in ['..', '-']:
    sys.exit()

path_to_dir = lib.read_frecency_db()

# increment target dir

target_path = os.path.join(*sys.argv[1:])
path_to_dir[target_path].count += 1
path_to_dir[target_path].path = target_path

# write new frecency db

with open(lib.db_path, 'w') as f:
    f.write('\n'.join([repr(dir_) for path, dir_ in path_to_dir.items()]))
