#! /usr/bin/python3

from mutagen import File
from os import chdir, getcwd, listdir, makedirs, rename
from os.path import isfile, join
import sys

def make_valid(filename):
    '''
        Takes a string and returns its valid version for a file name
    '''
    return ''.join(char for char in filename if char.isalnum() or char in '._- ')


def organize():
    files = [file for file in listdir(getcwd()) if isfile(file)]
    file_counter = 0
    for file in files:
        song = File(file, easy=True)
        if song is not None:
            artist_name = song.get('artist', 'unknown_artist')
            artist_name = artist_name[0] if type(artist_name) == list else artist_name
            artist_name = make_valid(artist_name)

            album_name = song.get('album', 'unknown_album')
            album_name = album_name[0] if type(album_name) == list else album_name
            album_name = make_valid(album_name)

            print('Processing now: File name: %s; Artist name: %s; Album name: %s' %(file, artist_name, album_name))

            song_directory = join(artist_name, album_name)
            makedirs(song_directory, exist_ok=True)
            rename(file, join(song_directory, file))

            file_counter += 1

    return file_counter

def usage_msg(argv):
    print('Usage: %s [<path_to_musics_folder>]' %(argv[0]))
    print('To work in the current directory, leave the path in blank.')

def main():
    if len(sys.argv) > 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        usage_msg(sys.argv)
        sys.exit(2)

    if len(sys.argv) == 2:
        try:
            chdir(sys.argv[1])
        except FileNotFoundError as exception:
            print('Error: %s' %(exception))
            sys.exit(1)

    file_counter = organize()
    print('Job done. %d files processed.' %(file_counter))

if __name__ == '__main__':
    main()
