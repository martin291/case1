#!/usr/bin/env python3
class Patient(object):

    def __init__(self, name, age, doctor):
        self.name = name
        self.age = age
        self.doctor = doctor

    def __str__(self):
        p = []
        p.append('Name: {:s}'.format(self.name))
        p.append('Age: {:d}'.format(self.age))
        p.append('Doctor: {:s}'.format(self.doctor))
        return '\n'.join(p)

class Ward(object):

    def __init__(self):
        self.d = {}

    def add(self, p):
        self.d[p.name] = p

    def remove(self, name):
        if name in self.d:
            del(self.d[name])

    def lookup(self, name):
        try:
            return self.d[name]
        except KeyError:
            return None

def main():
    p1 = Patient('Mary', 34, 'James Kildare')
    p2 = Patient('Wendy', 40, 'Gregory House')

    w = Ward()

    w.add(p1)
    w.add(p2)

    p = w.lookup('Mary')
    assert(isinstance(p, Patient))
    assert(p.name == 'Mary')
    assert(p.age == 34)

    w.remove('Mary')
    p = w.lookup('Mary')
    assert(p is None)

if __name__ == '__main__':
    main()
