#!/usr/bin/env python3
class MP3Track(object):

    def __init__(self, title, duration, l):
        self.title = title
        self.duration = int(duration)
        if l is None:
            self.artists = []
        else:
            self.artists = l

    def __str__(self):
        track = []
        track.append('Title: {}'.format(self.title))
        track.append('By: {}'.format(', '.join(self.artists)))
        track.append('Duration: {}'.format(self.duration))
        return '\n'.join(track)

class MP3Collection(object):

    def __init__(self):
        self.d = {}
        self.art = {}
        self.l = []

    def add(self, track):
        self.d[track.title] = track
        for c in track.artists:
            if c not in self.art.keys():
                self.art[c] = [track]
            else:
                self.art[c].append(track)
        if track not in self.l:
            self.l.append(track)

    def remove(self, name):
        if name in self.d:
            del(self.d[name])

    def lookup(self, name):
        try:
            return self.d[name]
        except KeyError:
            return None

    def get_mp3s_by_artist(self, name):
        if name in self.art:
            return self.art[name]
        else:
            return None

    def __add__(self, other):
        n = MP3Collection()
        new_list = (self.l + other.l)
        tracks = []
        for c in new_list:
            if c not in tracks:
                tracks.append(c)
        n.list_add(tracks)
        return n

    def list_add(self, l):
        for c in l:
            if c.title not in self.d.keys():
                self.d[c.title] = c

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    c1 = MP3Collection()
    c1.add(t1)
    c1.add(t2)

    c2 = MP3Collection()
    c2.add(t3)

    # Make a new collection from two existing ones
    c3 = c1 + c2
    #print(c3)
    assert(isinstance(c3, MP3Collection))
    assert(c3 is not c1)
    assert(c3 is not c2)

if __name__ == '__main__':
    main()
