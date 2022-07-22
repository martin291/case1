#!/usr/bin/env python3
import sys

def amount(l):
    N = len(l) % 3
    if len(l) == 3:
        return (sum(l) - min(l))
    else:
        i = 3
        total = 0
        while (i + N) != len(l) + 3:
            batch = l[:3]
            total = total + (sum(batch) - min(batch))
            i = i + 3
        return total + min(l)

for line in sys.stdin:
    list = line.strip().split()
    cakes = []
    for c in list:
        n = int(c)
        cakes.append(n)
    if len(cakes) >= 3:
        total = amount(cakes)
        print(total)
    else:
        print(sum(cakes))
