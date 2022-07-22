#!/usr/bin/env python3
class Student(object):

    def __init__(self, name, address, sid):
        self.name = name
        self.address = address
        self.sid = sid
        self.marks = {}

    def __str__(self):
        r = []
        r.append('Name: {:s}'.format(self.name))
        r.append('Address: {:s}'.format(self.address))
        r.append('ID: {:d}'.format(self.sid))
        r.append('Average mark: {:.2f}'.format(self.average_mark()))
        return '\n'.join(r)

    def add_mark(self, module, mark):
        self.marks[module] = mark

    def get_mark(self, s):
        if s in self.marks:
            return self.marks[s]
        return 'Not registered for module'

    def average_mark(self):
        if not self.marks:
            return 0
        return (sum([c for c in self.marks.values()]) / len(self.marks.values()))

    def __eq__(self, other):
        return self.average_mark() == other.average_mark()

    def __gt__(self, other):
        return self.average_mark() > other.average_mark()

    def __lt__(self, other):
        return self.average_mark() < other.average_mark()

def main():

    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)
    s3 = Student('Mikhail Tal', 'Belfast', 17884786)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)
    print(s1)

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)
    print(s2)

    s3.add_mark('CA103', 60)
    s3.add_mark('CA106', 50)
    print(s3)

    assert(s1 == s3)
    assert(s1 < s2)
    assert(s2 > s3)

if __name__ == '__main__':
    main()
