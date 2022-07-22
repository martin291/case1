#!/usr/bin/env python3
import sys

V = sys.stdin.readline()
paths_list = []
for line in sys.stdin:
   x, y = line.strip().split()
   if x not in paths_list or paths_list == []:
      paths_list.append(x)
   if y not in paths_list or paths_list == []:
      paths_list.append(y)

print(paths_list)
