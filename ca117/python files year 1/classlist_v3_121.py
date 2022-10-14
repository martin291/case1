#!/usr/bin/env python3
class Student(object):

    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid
        self.marks = {}
        self.l = []

    def __str__(self):
        r = []
        r.append('Name: {:s}'.format(self.name))
        r.append('Address: {:s}'.format(self.address))
        r.append('ID: {:d}'.format(self.sid))
        return '\n'.join(r)

    def add_mark(self, module, mark):
        self.marks[module] = mark
        self.l.append(module)

    def get_mark(self, s):
        if s in self.marks:
            return self.marks[s]
        return 'Not registered for module'

def sort_on(c):
    return c.sid

class Classlist(object):

    def __init__(self):
        self.d = {}
        self.lp = []

    def add(self, s):
        self.d[s.sid] = s
        self.lp += s.l

    def remove(self, sid):
        del(self.d[sid])

    def lookup(self, sid):
        if sid in self.d:
            return self.d[sid]
        else:
            return None

    def __str__(self):
        slist = ['{}'.format(c) for c in sorted(self.d.values(), key=sort_on)]
        return '\n'.join(slist)

    def least_popular_module(self):
        notpop = None
        i = 0
        while i < len(self.lp) - 1:
            if self.lp.count(self.lp[i]) < self.lp.count(self.lp[i + 1]):
                notpop = self.lp[i]
            i = i + 1
        return notpop

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)
    s3 = Student('Mikhail Tal', 'Belfast', 17884786)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)

    s3.add_mark('CA103', 80)
    s3.add_mark('CA106', 90)

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl.least_popular_module())

if __name__ == '__main__':
    main()
