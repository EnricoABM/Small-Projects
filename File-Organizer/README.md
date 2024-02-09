# File Organizer

[<<< Back the home](/README.md)

## Project Description

A project created using `os` module from python 3.11 to organize files.

This project consists of a script to organize files in a directory, based on files extensions (file.ext), for each extension a directory will be created, and all files will be moved to their respective folder.

### How to use

The user can run this script in terminal, using:

 ```python3.11 -m file_organizer [path, new_files_prefix]```.

The arguments `path` and `new_files_prefix` are optional, `path` is the path of the directory that will be organized, and `new_files_prefix` is the prefix for the new directories that will be created (prefix_ext). Both must receive a string.

### Using in your code

To implement the file organizer in your code, use: `from file_organizer import Organizer` to import `Organizer` class, it has the same optional arguments mentioned before (`path` and `new_files_prefix`). If omitted, the script will organize the current directory and the prefix used will be 'files_ext'.

To test the script, the `create_random_files` module creates some files to test the File Organizer. To do this, use the `create_aleartory_files` function, this takes an optional argument `path`, this being the path where the example files will be created, if omitted, the files will be created in current directory.

### Files

| Files | Link |
|-------|------|
| file_organizer.py | [Go to file](files/file_organizer.py) |
| create_aleatory_files.py | [Go to file](files/create_aleartory_files.py) |

---
