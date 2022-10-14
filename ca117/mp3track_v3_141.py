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

    def add_artist(self, artist):
        if artist not in self.artists:
            self.artists.append(artist)

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197)

    print(t1)
    print(t2)

    t2.add_artist('Lady Gaga')
    print(t2)

    t2.add_artist('Bradley Cooper')
    print(t2)

if __name__ == '__main__':
    main()
