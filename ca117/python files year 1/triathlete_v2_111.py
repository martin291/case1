#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.time = 0
        self.cycle = 0
        self.swim = 0
        self.run = 0

    def add_time(self, race, time):
        if race == "cycle":
            self.cycle = time
        elif race == "swim":
            self.swim = time
        elif race == "run":
            self.run = time
        self.time = self.time + time

    def get_time(self, race):
        if race == "cycle":
            return (self.cycle)
        elif race == "swim":
            return (self.swim)
        elif race == "run":
            return (self.run)

    def __str__(self):
        list = []
        list.append('Name: {}'.format(self.name))
        list.append('ID: {}'.format(self.tid))
        list.append('Race time: {}'.format(self.time))
        return '\n'.join(list)

def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()
