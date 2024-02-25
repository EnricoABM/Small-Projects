""" This module is for testing the file organizer"""

from itertools import product
from pathlib import Path


def create_aleartory_files(path: str = 'files'):
    ''' Create some files in the directory for testing '''
    extension = ['txt', 'js',
                 'html', 'css',
                 'py', 'pdf',
                 'jpg', 'png',
                 'jpeg', 'md']

    files_name = ['important_document', 'project_plan',
                  'README', 'meeting_minutes',
                  'budget_sheet', 'research_report',
                  'invoice', 'presentation_slide',
                  'todo_list', 'contact_directory']

    for file, ext in product(files_name, extension):
        example_dir_files = Path(path) / (file + '.' + ext)
        print(example_dir_files)
        example_dir_files.touch()


if __name__ == "__main__":
    create_aleartory_files()
