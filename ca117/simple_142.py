#!/usr/bin/env python3
import sys

for line in sys.stdin:
    word = line.strip()
    unique = []
    for c in word:
        if c not in unique:
            unique.append(c)
    simplicity = len(unique)
    if simplicity > 2:
        deletions = -2 + simplicity
        print(deletions)
    else:
        print(0)
