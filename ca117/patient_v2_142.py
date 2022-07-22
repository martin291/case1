#!/usr/bin/env python3
class Patient():

    def __init__(self, name, age, doctor, l):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.med = []
        self.med = l

    def __str__(self):
        p = []
        p.append('Name: {:s}'.format(self.name))
        p.append('Age: {:d}'.format(self.age))
        p.append('Medications: {}'.format(", ".join(self.med)))
        p.append('Doctor: {:s}'.format(self.doctor))
        return '\n'.join(p)

def main():
    p1 = Patient('Mary', 34, 'James Kildare', ['aspirin'])
    p2 = Patient('Wendy', 40, 'Gregory House', ['penicillin', 'nexium'])

    print(p1)
    print(p2)

if __name__ == '__main__':
    main()
