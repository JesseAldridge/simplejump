import os
import collections
import time

db_path = os.path.expanduser('~/simplejump.txt')

def read_frecency_db():
    ' Read frecency db.  Return mapping from paths to Dirs. '

    class Dir:
        ' Calculate frecency for each Dir. '

        def __init__(self, line=None):
            self.count, self.timestamp, self.path = (
                line.split(' ', 2) if line else [0, time.time(), None])
            self.count = int(self.count)
            self.frecency = frecency(self.count, self.timestamp)
        def __repr__(self):
            return '{0} {1} {2}'.format(self.count, self.timestamp, self.path)

    if not os.path.exists(db_path):
        with open(db_path, 'w'):
            pass
    with open(db_path, 'r') as f:
        path_to_dir = collections.defaultdict(Dir)
        for line in f.read().splitlines():
            dir_ = Dir(line)
            path_to_dir[dir_.path] = dir_
    return path_to_dir


def frecency(count, timestamp):
    delta = (time.time() - float(timestamp)) * .00001
    result = count - delta
    # print 'count:', count
    # print 'timestamp:', timestamp
    # print 'result:', result
    # print
    return result


if __name__ == '__main__':
    path_to_dir = read_frecency_db()
    for path, dir_ in sorted(
        path_to_dir.items(), key=lambda t: t[-1].frecency)[:10]:
        print path, dir_.frecency

    desired_order = [
        [7, 1360338356.34], [8, 1360099202.01], [5, 1360338356.34]]
    actual_order = sorted(
        desired_order, key=lambda l: frecency(*l), reverse=True)

    print 'desired:', desired_order
    print 'actual:', actual_order
    assert desired_order == actual_order
