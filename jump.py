#!/usr/bin/python

import sys
import os

import utils

# Print the most frecent dir matching the query.

query = sys.argv[-1]
if query in ['..']:
    sys.exit()

path_to_dir = utils.read_and_boost(query)

for dir_ in sorted(
    path_to_dir.values(), key=lambda dir_: dir_.score, reverse=True):
    if os.path.isdir(dir_.path) and query.lower() in dir_.path.lower():
        print dir_.path
        break
