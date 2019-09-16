import os
import collections
import time
import datetime
import sys

DB_PATH = os.path.expanduser('~/sj_db.txt')

class Dir:
  ' Calculate frecency for each Dir. '

  def __init__(self, line=None):
    self.count, self.timestamp, self.path = [0, time.time(), None]
    if line:
      self.count, self.timestamp, self.path = line.split(' ', 2)
    self.count = int(self.count)
    self.timestamp = float(self.timestamp)
    self.score = frecency(self.count, self.timestamp)

  def serialize(self):
    return '%i %s %s' % (self.count, str(self.timestamp), self.path)

  def print_(self):
    print '{0:<15}| {1:<10}| count: {2}| boost: {3}| score: {4}'.format(
      '...' + self.path[-12:], str(
         datetime.timedelta(seconds=time.time()) -
         datetime.timedelta(seconds=self.timestamp)).split(',', 1)[0],
      self.count, self.boost, int(self.score))

def read_frecency_db(db_path=DB_PATH):
  ' Read frecency db.  Return mapping from paths to Dirs. '

  if not os.path.exists(db_path):
    open(db_path, 'w').close()

  f = open(db_path, 'r')
  try:
    path_to_dir = {}
    for line in f.read().splitlines():
      dir_ = Dir(line)
      if dir_.path not in path_to_dir:
        path_to_dir[dir_.path] = dir_
  finally:
    f.close()

  return path_to_dir

def read_and_boost(query, db_path=DB_PATH):
  ' Boost dirs with a path that case-sensitive matches query. '

  path_to_dir = read_frecency_db(db_path)
  for dir_ in path_to_dir.values():
    boost = 0.
    if query in os.path.basename(dir_.path):
      boost = 4.
    elif query.lower() in os.path.basename(dir_.path).lower():
      boost = 3
    elif query in dir_.path:
      boost = 1.
    dir_.boost = boost
    dir_.score += dir_.count * boost
  return path_to_dir

def frecency(count, timestamp):
  ' Take into account frequency and recency. '

  delta = (time.time() - timestamp) ** .4
  result = count * 3 - delta
  return result


if __name__ == '__main__':

  # Use test db to check frecency.

  read_and_boost('Impact')

  for query, desired_order in [
    ('impact', ['server_h', 'server_o', 'a', 'test impact', 'Impact', 'b']),
    ('Impact', ['server_h', 'server_o', 'Impact', 'test impact', 'a', 'b']),
    ('server', ['server_h', 'server_o', 'a', 'test impact', 'b', 'Impact'])]:
    path_to_dir = read_and_boost(query, 'test_db.txt')
    dirs = sorted(path_to_dir.values(), key=lambda d: d.score)[::-1]
    print 'query:', query
    print 'desired:', desired_order
    print 'actual:'
    for dir_ in dirs:
      dir_.print_()
    print
    sys.stdout.flush()
    assert desired_order == [os.path.basename(d.path) for d in dirs]
