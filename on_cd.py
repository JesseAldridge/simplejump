#!/usr/bin/python

import sys
import os

import utils

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
