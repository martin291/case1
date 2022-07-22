#!/usr/bin/env python3
class Patient():

    def __init__(self, name, age, doctor, l=None):
        self.name = name
        self.age = age
        self.doctor = doctor
        if l is None:
            self.med = []
        else:
            self.med = l

    def __str__(self):
        p = []
        p.append('Name: {:s}'.format(self.name))
        p.append('Age: {:d}'.format(self.age))
        p.append('Medications: {}'.format(", ".join(self.med)))
        p.append('Doctor: {:s}'.format(self.doctor))
        return '\n'.join(p)

class Ward(object):

    def __init__(self):
        self.d = {}
        self.m = {}

    def add(self, p):
        self.d[p.name] = p
        for c in p.med:
            if c not in self.m.keys():
                self.m[c] = [p]
            else:
                self.m[c].append(p)

    def remove(self, name):
        if name in self.d:
            del(self.d[name])

    def lookup(self, name):
        try:
            return self.d[name]
        except KeyError:
            return None

    def get_patients_by_medication(self, med):
        if med in self.m:
            return self.m[med]
        else:
            return None

def main():
    p1 = Patient('Mary', 34, 'James Kildare', ['aspirin'])
    p2 = Patient('Wendy', 40, 'Gregory House', ['penicillin', 'nexium'])
    p3 = Patient('Sam', 42, 'Gregory House', ['nexium'])

    w = Ward()
    w.add(p1)
    w.add(p2)
    w.add(p3)

    # Retrieve all patients on nexium
    patient_list = w.get_patients_by_medication('nexium')
    assert(len(patient_list) == 2)
    assert(p1 not in patient_list)
    assert(p2 in patient_list)
    assert(p3 in patient_list)

if __name__ == '__main__':
    main()
