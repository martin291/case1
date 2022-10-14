#!/usr/bin/env python3
import sys

def intersection(a, b):
    for c in a:
        if c in b:
            return(a.index(c), b.index(c))

for line in sys.stdin:
    a, b = line.strip().split()
    i, j = intersection(a, b)
    lines = ['.' * i + c + '.' * (len(a) - 1 - i) for c in b]
    lines[j] = a
    print('\n'.join(lines))
