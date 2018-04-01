# Archivist
A simple program that helps you organizing your musics

## Getting Started
Follow this instructions to install the program in your machine.

### Prerequisites
This program requires [Python 3](https://www.python.org/downloads/) in order to run. Check how to install
the latest version in your platform.

The only third-party package that's being used is [Mutagen](https://mutagen.readthedocs.io/en/latest/),
a library used to handle the files' tags in order to extract information such as
the song's band/artist and its album. To install it:

`pip install mutagen==1.40.0`

### Installing
The only file you'll need is [archivist.py](archivist.py). To download and install it,
folow these steps:

`wget https://raw.githubusercontent.com/JeffersonCarvalh0/Archivist/master/archivist.py` - To download it
`chmod u+x archivist.py` - To give it permission to execute
`sudo mv archivist.py /usr/bin/archivist` - To allow it to be executed globally

### Usage
Just type `archivist` anywhere you like, and it should do the job.
Alternatively, you can give a directory as an argument.

The program will search for music files in the given directory, separating the files
by artist and album, after getting this info from the file's tag.

### Uninstalling
To uninstall, just type `sudo rm /usr/bin/archivist` in the terminal.

## Built With
* [Mutagen](https://mutagen.readthedocs.io/en/latest/) - A Python module to handle audio metadata

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
