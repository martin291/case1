#!/usr/bin/env python3
class MP3Track(object):

    def __init__(self, title, duration, l=None):
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

    def add(self, track):
        self.d[track.title] = track
        for c in track.artists:
            if c not in self.art.keys():
                self.art[c] = [track]
            else:
                self.art[c].append(track)

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

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    c = MP3Collection()

    c.add(t1)
    c.add(t2)
    c.add(t3)

    # Retrieve all MP3Tracks from the collection by Lady Gaga
    tracklist = c.get_mp3s_by_artist('Lady Gaga')
    assert(len(tracklist) == 2)
    assert(t2 in tracklist)
    assert(t3 in tracklist)

if __name__ == '__main__':
    main()
