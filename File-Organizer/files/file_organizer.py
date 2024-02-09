""" Module to organize files in a diretory"""

import os
import shutil
import sys


class Organizer:
    def __init__(self,
                 path: str = os.path.abspath('.'),
                 new_files_prefix: str = 'files'):
        """ Create a file organizer

        :param path: Path of the folder where the files are located, if not
        passed, it will be carried out in the current folder.
        :param new_files_prefix: Prefix of the new folders that will be
        created to organize the files."""
        self.dir_path = path
        self.files_in_dir = os.listdir(self.dir_path)
        self.files_dir_path = os.path.join(self.dir_path, new_files_prefix)
        self.extensions = self.__discover_extensions()

    def __discover_extensions(self) -> set:
        """ Cycles through all files in the folder,
        and stores each extension

        :return: A set containing all extensions """

        files_extensions = set()
        # Scan all files in the folder to discover extensions;
        for file in self.files_in_dir:
            if os.path.basename(__file__) == file:
                continue
            # Checks whether it is a file or a folder, it must receive
            # the full path, otherwise they will all be files;
            if not os.path.isdir(os.path.join(self.dir_path, file)):
                # Separate the file path from the extension and then
                # store it in a set;
                _, ext = os.path.splitext(file)
                files_extensions.add(ext)
        # Return the set;
        return files_extensions

    def create_dirs(self) -> None:
        """ Creates a directory for each extension found """

        # Go through all extensions and create a folder for each type;
        for ext in self.extensions:
            # Previously a dot was placed between the prefix and the extension,
            # Replace with an underscore to create folders, if any, will
            # not raise an error;
            os.makedirs(self.files_dir_path + ext.replace('.', '_'),
                        exist_ok=True)

    def move_files(self) -> None:
        """ Move each file to its respective folder """

        for file in self.files_in_dir:
            if os.path.basename(__file__) == file:
                continue
            # Check if it is a file or a folder, it must receive the path
            # complete, otherwise they will all be files;
            if not os.path.isdir(os.path.join(self.dir_path, file)):
                # Separation of file path from file extension;
                _, ext = os.path.splitext(os.path.join(self.dir_path, file))
                # Creation of the original file path;
                file_path = os.path.join(self.dir_path, file)
                # Creation of the new file path;
                new_file_dir_path = os.path.join(
                    self.files_dir_path + ext.replace('.', '_'),
                    file)
                shutil.move(file_path, new_file_dir_path)


if '__main__' == __name__:
    if len(sys.argv) > 1:
        try:
            arguments = sys.argv[1:]
            path = arguments[0]
            new_files_prefix = arguments[1]
            file_organizar = Organizer(
                path=path,
                new_files_prefix=new_files_prefix
                )
        except IndexError:
            file_organizar = Organizer(
                path=path)
    else:
        file_organizar = Organizer()
    file_organizar.create_dirs()
    file_organizar.move_files()
