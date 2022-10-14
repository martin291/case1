#!/usr/bin/env python3
class MP3Track(object):

    def __init__(self, title, duration, l=None):
        self.title = title
        self.duration = int(duration)

    def __str__(self):
        track = []
        track.append('Title: {}'.format(self.title))
        track.append('Duration: {}'.format(self.duration))
        return '\n'.join(track)

class MP3Collection(object):

    def __init__(self):
        self.d = {}

    def add(self, track):
        self.d[track.title] = track

    def remove(self, name):
        if name in self.d:
            del(self.d[name])

    def lookup(self, name):
        try:
            return self.d[name]
        except KeyError:
            return None

def main():
    t1 = MP3Track('Fools Gold', 604)
    t2 = MP3Track('Shallow', 197)
    t3 = MP3Track('Telephone', 220)

    c = MP3Collection()

    c.add(t1)
    c.add(t2)
    c.add(t3)

    t = c.lookup('Fools Gold')
    assert(isinstance(t, MP3Track))
    assert(t.title == 'Fools Gold')
    assert(t.duration == 604)

    c.remove('Fools Gold')
    t = c.lookup('Fools Gold')
    assert(t is None)

if __name__ == '__main__':
    main()
