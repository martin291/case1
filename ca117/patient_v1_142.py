#!/usr/bin/env python3
class Patient():

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


def main():
    p1 = Patient('Mary', 34, 'James Kildare')
    p2 = Patient('Wendy', 40, 'Gregory House')

    assert(p1.name == 'Mary')
    assert(p1.age == 34)
    assert(p1.doctor == 'James Kildare')

    print(p1)
    print(p2)

if __name__ == '__main__':
    main()
