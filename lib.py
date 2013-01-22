import os
import collections
import time

db_path = os.path.expanduser('~/simplejump.txt')

def read_frecency_db():
    # Calculate freceny for each Dir.

    class Dir:
        def __init__(self, line=None):
            self.count, self.timestamp, self.path = (
                line.split(' ', 2) if line else [0, time.time(), None])
            self.count = int(self.count)
            delta = (time.time() - float(self.timestamp)) * .001
            self.frecency = float(self.count) / delta if delta > 0 else float(self.count)
        def __repr__(self):
            return '{0} {1} {2}'.format(self.count, self.timestamp, self.path)

    # Read frecency db.  Return mapping from paths to Dirs.

    if not os.path.exists(db_path):
        with open(db_path, 'w'):
            pass
    with open(db_path, 'r') as f:
        path_to_dir = collections.defaultdict(Dir)
        for line in f.read().splitlines():
            dir_ = Dir(line)
            path_to_dir[dir_.path] = dir_
    return path_to_dir

if __name__ == '__main__':
    path_to_dir = read_frecency_db()
    print 'path_to_dir:', path_to_dir.items()
    for path, dir_ in sorted(
        path_to_dir.items(), key=lambda t: t[-1].frecency):
        print path, dir_.frecency
