#!/usr/bin/env python3
class Student(object):

    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid

    def __str__(self):
        r = []
        r.append('Name: {:s}'.format(self.name))
        r.append('Address: {:s}'.format(self.address))
        r.append('ID: {:d}'.format(self.sid))
        return '\n'.join(r)

def sort_on(c):
    return c.sid

class Classlist(object):

    def __init__(self):
        self.d = {}

    def add(self, s):
        self.d[s.sid] = s

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

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)
    s3 = Student('Mikhail Tal', 'Belfast', 17884786)

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl)

if __name__ == '__main__':
    main()
