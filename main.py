#! /usr/bin/python3

from mutagen import File
from os import getcwd, listdir, makedirs, rename
from os.path import isfile, join

def make_valid(filename):
    '''
        Takes a string and returns its valid version for a file name
    '''
    return ''.join(char for char in filename if char.isalnum() or char in '._- ')

files = [file for file in listdir(getcwd()) if isfile(file)]

for file in files:
    song = File(file, easy=True)
    if song is None:
        continue
    artist_name = make_valid(song.get('artist', 'unknown_artist')[0])
    album_name = make_valid(song.get('album', 'unknown_album')[0])
    song_directory = join(artist_name, album_name)
    makedirs(song_directory, exist_ok=True)
    rename(file, join(song_directory, file))
