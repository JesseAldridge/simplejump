#!/usr/bin/python

import sys
import os

import utils

# ----------

# sys.argv: ['.../on_cd.py', pwd, target_dir]

# db format
# <count> <time> <path>
# 2 1358624598.17 ~/foo/bar
# 1 1358624611.5 ~/foo/bar/baz

# ----------

if sys.argv[-1] in ['..', '-']:
    sys.exit()

path_to_dir = utils.read_frecency_db()

# increment target dir

target_path = os.path.abspath(os.path.join(*sys.argv[1:]))
path_to_dir[target_path].count += 1
path_to_dir[target_path].path = target_path

# print 'target_path: {0}'.format(target_path)

# write new frecency db

with open(utils.DB_PATH, 'w') as f:
    f.write('\n'.join([
        dir_.serialize() for path, dir_ in path_to_dir.items()]))
