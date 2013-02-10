import time

def frecency(count, timestamp):
    delta = (time.time() - float(timestamp)) * .00001
    result = count - delta
    # print 'count:', count
    # print 'timestamp:', timestamp
    # print 'result:', result
    # print
    return result

if __name__ == '__main__':
    desired_order = [
        [7, 1360338356.34], [8, 1360099202.01], [5, 1360338356.34]]
    actual_order = sorted(
        desired_order, key=lambda l: frecency(*l), reverse=True)

    print desired_order
    print actual_order
    assert desired_order == actual_order