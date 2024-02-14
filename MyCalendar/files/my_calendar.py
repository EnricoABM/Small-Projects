"""My Calendar

A Task manager application in terminal, for viewing, navigating through months,
adding events, and displaying them.

That project's idea is from chatgpt
"""

from my_calendar_types import MyCalendar
import os
import json
from pprint import pprint


def menu():
    print('-' * 50)
    print(f'{" " * 23}MENU{" " * 23}')
    print('-' * 50)
    print('[1] - Create MyCalendar')
    print('[2] - Show MyCalendar')
    print('[3] - Create Tasks')
    print('[4] - Update a Task')
    print('[5] - Finish a Task')
    print('[6] - Delete a Task')
    print('[7] - Save in File')
    print('[8] - Load in File')
    print('[9] - Exit')
    print('-' * 50)


def menu_show():
    print('-' * 50)
    print(f'{" " * 23}MENU{" " * 23}')
    print('-' * 50)
    print('[1] - Show all calendar')
    print('[2] - Show a month')
    print('[3] - Show all tasks')
    print('-' * 50)


def clear():
    os.system('clear')


def create_calendar() -> MyCalendar:
    year = input('Enter with calendar year: ')
    while not year.isdigit():
        print('Enter with valid option!!!')
        year = input('Enter with calendar year: ')
    calendar = MyCalendar(int(year))
    return calendar


def show_calendar(calendar: MyCalendar):
    calendar.show_calendar()


def show_month(calendar: MyCalendar, month: int):
    calendar.show_month(month)


def show_tasks(calendar: MyCalendar):
    calendar.show_all_tasks()


def create_task(calendar: MyCalendar):
    name = input('Enter a name: ')
    month = valid_option(
        list(map(str, range(1, 13))),
        'Enter a month number: '
    )
    day = valid_option(
        list(map(str, range(1, 32))),
        'Enter a day: '
    )
    describe = input('Enter a describe: ')
    calendar.create_task(name, int(month), int(day), describe)


def update_task(calendar: MyCalendar):
    id = input('Enter a ID: ')
    while not id.isdigit():
        print('Enter with valid option!!!')
        id = input('Enter a ID: ')
    name = input('Enter a name: ')
    option_list = list(map(str, range(1, 13))) + ['']
    month = valid_option(
        option_list,
        'Enter a month number: '
    )
    option_list = list(map(str, range(1, 32))) + ['']
    day = valid_option(
        option_list,
        'Enter a day: '
    )
    describe = input('Enter a describe: ')
    calendar.update_task(int(id), name, int(month), int(day), describe)


def finish_task(calendar: MyCalendar):
    id = input('Enter a ID: ')
    while not id.isdigit():
        print('Enter with valid option!!!')
        id = input('Enter a ID: ')
    calendar.finish_task(int(id))


def delete_task(calendar: MyCalendar):
    id = input('Enter a ID: ')
    while not id.isdigit():
        print('Enter with valid option!!!')
        id = input('Enter a ID: ')
    calendar.delete_task(int(id))


def valid_option(value_set, msg='>>> '):
    input_value = input(msg)
    while input_value not in value_set:
        print('Enter with valid option!!!')
        input_value = input(msg)
    return input_value


def save_in_file(calendar: MyCalendar, file_name='MyCalendar.json'):
    ABSOLUTE_FILE_PATH = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            file_name
        )
    )
    with open(ABSOLUTE_FILE_PATH, 'w') as file:
        json.dump(
            calendar.load_data(),
            file,
            ensure_ascii=False,
            indent=2)


def load_in_file(
        calendar: MyCalendar,
        file_name='MyCalendar.json'):
    ABSOLUTE_FILE_PATH = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            file_name
        )
    )
    with open(ABSOLUTE_FILE_PATH, 'r') as file:
        data = json.load(file)
        calendar.restore_data(data)


def check_file_option(calendar: MyCalendar, func):
    file_option = input(
        'Default name: "MyCalendar.json", ' +
        'pless enter to use default name...\n' +
        'Enter a file name: '
        )
    if file_option == '':
        func(calendar)
    else:
        file_option += '.json'
        func(calendar, file_option)


my_calendar = None

if __name__ == '__main__':
    while True:
        clear()
        menu()
        res = valid_option(
            '123456789',
            'Enter a option: ')

        if res == '1':
            if my_calendar is not None:
                print('There is a my calendar already create.')
                want_overwrite = valid_option(
                    'yn',
                    'Do you want overwrite? [Y/n]: ')

                if want_overwrite.lower() == 'y':
                    my_calendar = create_calendar()

            elif my_calendar is None:
                my_calendar = create_calendar()
        elif res == '2':
            if my_calendar is not None:
                menu_show()
                show_option = valid_option(
                    '123',
                    'Enter a option: '
                )

                if show_option == '1':
                    show_calendar(my_calendar)
                elif show_option == '2':
                    month = valid_option(
                        ['1', '2', '3',
                         '4', '5', '6',
                         '7', '8', '9',
                         '10', '11', '12'],
                        'Enter a month number: '
                    )
                    show_month(my_calendar, int(month))
                elif show_option == '3':
                    show_tasks(my_calendar)
            elif my_calendar is None:
                print('You need to create a MyCalendar')
        elif res == '3':
            if my_calendar is not None:

                create_task(my_calendar)

            elif my_calendar is None:
                print('You need to create a MyCalendar')
        elif res == '4':
            if my_calendar is not None:
                show_tasks(my_calendar)
                update_task(my_calendar)
            elif my_calendar is None:
                print('You need to create a MyCalendar')
        elif res == '5':
            if my_calendar is not None:
                show_tasks(my_calendar)
                finish_task(my_calendar)
            elif my_calendar is None:
                print('You need to create a MyCalendar')
        elif res == '6':
            if my_calendar is not None:
                show_tasks(my_calendar)
                delete_task(my_calendar)
            elif my_calendar is None:
                print('You need to create a MyCalendar')
        elif res == '7':
            if my_calendar is not None:
                check_file_option(my_calendar, save_in_file)
            elif my_calendar is None:
                print('You need to create a MyCalendar')
        elif res == '8':
            if my_calendar is not None:
                print('There is a my calendar already create.')
                want_overwrite = valid_option(
                    'yn',
                    'Do you want overwrite? [Y/n]: ')

                if want_overwrite.lower() == 'y':
                    check_file_option(my_calendar, load_in_file)

            elif my_calendar is None:
                my_calendar = MyCalendar(2000)
                load_in_file(my_calendar)
        elif res == '9':
            break
        print()
        pprint(my_calendar.__dict__)
        input('Pless enter to continue...')
