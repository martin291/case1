#!/usr/bin/env python3
class MP3Track(object):

    def __init__(self, title, duration, l=None):
        self.title = title
        self.duration = int(duration)
        mins = self.duration // 60
        secs = self.duration % 60
        if secs < 10:
            secs = '0' + str(secs)
        self.mins = str(mins) + ':' + str(secs)
        if l is None:
            self.artists = []
        else:
            self.artists = l

    def __str__(self):
        track = []
        track.append('Title: {}'.format(self.title))
        track.append('By: {}'.format(', '.join(self.artists)))
        track.append('Duration: {}'.format((self.mins)))
        return '\n'.join(track)

    def add_artist(self, artist):
        if artist not in self.artists:
            self.artists.append(artist)

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])
    t4 = MP3Track('Her Majesty', 34, ['The Beatles'])
    t5 = MP3Track('Seven Seconds', 7, ['Neneh Cherry'])

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)

if __name__ == '__main__':
    main()
