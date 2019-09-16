#!/usr/bin/python

import sys
import os
import subprocess

import utils

if 'SIMPLE_JUMP_CD_CALLED' not in os.environ:
  sys.stderr.write(
    'simplejump: Something stole cd!\n'
    '(Did you install rvm recently?  Try removing it from your .bash_profile.)\n')
  proc = subprocess.Popen(['type', 'cd'], stdout=subprocess.PIPE)
  sys.stderr.write(proc.stdout.read())


def print_dir(query):

  # Print the most frecent dir matching the query.

  path_to_dir = utils.read_and_boost(query)
  paths = sorted(
    path_to_dir.values(), key=lambda dir_: dir_.score, reverse=True)
  for dir_ in paths:
    if os.path.isdir(dir_.path) and query.lower() in dir_.path.lower():
      print dir_.path
      break
  else:
    sys.stderr.write('no matching path found\n')
    print '.'

if len(sys.argv) == 1:
  print_dir('foo', 1)
else:
  query = sys.argv.pop()
  if query in ['..']:
    sys.exit()
  print_dir(query)
