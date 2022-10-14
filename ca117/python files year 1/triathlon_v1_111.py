#!/usr/bin/env python3
class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        list = []
        list.append('Name: {}'.format(self.name))
        list.append('ID: {}'.format(self.tid))
        return '\n'.join(list)

class Triathlon(object):

    def __init__(self):
        self.tri = {}

    def add(self, other):
        self.tri[other.tid] = other

    def remove(self, tid):
        del(self.tri[tid])

    def lookup(self, tid):
        if tid in self.tri:
            return self.tri[tid]
        else:
            return None

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)

if __name__ == '__main__':
    main()
