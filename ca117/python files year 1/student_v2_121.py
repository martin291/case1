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
        return '\n'.join(r)

    def add_mark(self, module, mark):
        self.marks[module] = mark

    def get_mark(self, s):
        if s in self.marks:
            return self.marks[s]
        return 'Not registered for module'

def main():

    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)
    print(s1.get_mark('CA103'))

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)
    print(s2.get_mark('CA117'))

if __name__ == '__main__':
    main()
