#!/usr/bin/env python3
import sys

for line in sys.stdin:
    x, y = line.strip().split()
    if int(x) > 0:
        if int(y) > 0:
            print('1')
        elif int(y) < 0:
            print('2')
    elif int(x) < 0:
        if int(y) > 0:
            print('4')
        elif int(y) < 0:
            print('3')