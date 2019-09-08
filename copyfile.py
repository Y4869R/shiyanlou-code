#!/usr/bin/env python3

# copy file
# author: mlgc4869
# date: 2019-09-08

import sys

if len(sys.argv) < 3:
    print("Wrong parameter")
    print("[Usage: ./copyfile.py file1 file2]")
    sys.exit()

f1 = open(sys.argv[1])
s = f1.read()
f1.close()

f2 = open(sys.argv[2], 'w')
f2.write(s)
f2.close()

