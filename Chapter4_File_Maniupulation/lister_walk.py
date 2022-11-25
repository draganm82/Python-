# list of file tree with os.walk

import sys
import os


def lister(root):  # for a root dir
    for (thisdir, subshere, fileshere) in os.walk(root):  # generate dirs in tree
        print('[' + thisdir + ']')
    for fname in fileshere:                          # print files in this dir
        # handle one file # add dir name prefix
        path = os.path.join(thisdir, fname)
        print(path)


if __name__ == '__main__':
    lister(sys.argv)    # dir name in cmdlines
