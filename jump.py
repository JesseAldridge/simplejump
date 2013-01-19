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

if sys.argv[-1] in ['..']:
    sys.exit()

path_to_dir = lib.read_frecency_db()
for _, dir_ in sorted(
    path_to_dir.items(), key=lambda t: t[-1].frecency, reverse=True):
    if sys.argv[-1].lower() in dir_.path.lower():
        if os.path.exists(dir_.path):
            print dir_.path
            break