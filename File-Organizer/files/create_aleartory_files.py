""" This module is for testing the file organizer"""

from itertools import product
import os


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
        example_dir_files = os.path.join(path, file + '.' + ext)
        with open(example_dir_files, 'a'):
            ...
