
from ntpath import join


def missing_no(num):
    start = 0
    end = 100
    return sorted(set(range(start, end + 1)).difference(num))