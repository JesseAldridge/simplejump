import os
import collections
import time
import datetime
import sys

DB_PATH = os.path.expanduser('~/sj_db.txt')

class Dir:
    ' Calculate frecency for each Dir. '

    def __init__(self, line=None):
        self.count, self.timestamp, self.path = (
            line.split(' ', 2) if line else [0, time.time(), None])
        self.count = int(self.count)
        self.timestamp = float(self.timestamp)
        self.score = frecency(self.count, self.timestamp)

    def serialize(self):
        return '{0} {1} {2}'.format(self.count, self.timestamp, self.path)

    def print_(self):
        print '{0:<15}| {1:<10}| count: {2}| boost: {3}| score: {4}'.format(
            '...' + self.path[-12:], str(
               datetime.timedelta(seconds=time.time()) - 
               datetime.timedelta(seconds=self.timestamp)).split(',', 1)[0],
            self.count, self.boost, int(self.score))

def read_frecency_db(db_path=DB_PATH):
    ' Read frecency db.  Return mapping from paths to Dirs. '

    if not os.path.exists(db_path):
        with open(db_path, 'w'):
            pass

    with open(db_path, 'r') as f:
        path_to_dir = collections.defaultdict(Dir)
        for line in f.read().splitlines():
            dir_ = Dir(line)
            path_to_dir[dir_.path] = dir_

    return path_to_dir

def read_and_boost(query, db_path=DB_PATH):
    ' Boost dirs with a path that case-sensitive matches query. '  

    path_to_dir = read_frecency_db(db_path)
    for dir_ in path_to_dir.values():
        boost = 0.
        if query in os.path.basename(dir_.path):
            boost = 3.
        elif query.lower() in os.path.basename(dir_.path).lower():
            boost = 2.
        elif query in dir_.path:
            boost = 1.
        dir_.boost = boost
        dir_.score += dir_.count * boost
    return path_to_dir

def frecency(count, timestamp):
    ' Take into account frequency and recency. '

    delta = (time.time() - timestamp) * .000005
    result = count - delta
    return result


if __name__ == '__main__':
    read_and_boost('Impact')

    for query, desired_order in [
        ('impact', ['a', 'test_impact', 'Impact', 'b']),
        ('Impact', ['Impact', 'test_impact', 'a', 'b'])]:
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
