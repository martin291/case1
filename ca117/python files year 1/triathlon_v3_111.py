#!/usr/bin/env python3
class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}

    def __str__(self):
        r = []
        r.append('Name: {:s}'.format(self.name))
        r.append('ID: {:d}'.format(self.tid))
        r.append('Race time: {:d}'.format(self.total_time()))
        return '\n'.join(r)

    def add_time(self, discipline, time_in_secs):
        self.times[discipline] = time_in_secs

    def get_time(self, d):
        if d in self.times:
            return self.times[d]
        else:
            return 'N/A'

    def total_time(self):
        if not self.times:
            return 0
        return sum([t for t in self.times.values()])

    def __gt__(self, other):
        return self.total_time() > other.total_time()

    def __eq__(self, other):
        return self.total_time() == other.total_time()

def sort_on(t):
    return t.name

class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, s):
        self.d[s.tid] = s

    def remove(self, tid):
        del(self.d[tid])

    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        else:
            return None

    def __str__(self):
        slist = ['{}'.format(t) for t in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(slist)

    def best(self):
        return min(self.d.values())

    def worst(self):
        return max(self.d.values())

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    #print(tn)
    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
