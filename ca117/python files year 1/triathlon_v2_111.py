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

def sort_on(t):
    return t.name

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

    def __str__(self):
        r = ['{}'.format(t) for t in sorted(self.tri.values(), key=sort_on)]
        return '\n'.join(r)

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
