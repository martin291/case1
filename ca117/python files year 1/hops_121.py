#!/usr/bin/env python3
import sys
class Graph(object):

    def __init__(self, V):
        self.adj = {}
        self.V = V
        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class BFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = [False for _ in range(g.V)]
        self.parent = [False for _ in range(g.V)]
        self.bfs(s)

    def bfs(self, s):
        queue = [s]
        self.marked[s] = True

        while queue:
            v = queue.pop(0)
            for w in self.adj[v]:
                if not self.marked[w]:
                    queue.append(w)
                    self.parent[w] = v
                    self.marked[w] = True

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        return path[::-1]

def main():

    V = int(sys.stdin.readline())
    #V = 7
    v = int(sys.argv[2])
    #print(v)
    N = int(sys.argv[3])
    #print(N)

    g = Graph(V)

    for line in sys.stdin:

        v, w = [int(t) for t in line.strip().split()]
        g.addEdge(v, w)

    paths = BFSPaths(g, 0)

    print(paths.pathTo(V))

if __name__ == '__main__':
    main()
