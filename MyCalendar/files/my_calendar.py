"""Command-Line-Calendar

Simple calendar application for viewing, navigating through months,
adding events, and displaying them

That project's idea is from chatgpt
"""

from types_my_calendar import MyCalendar
import os


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
    print('[7] - Save in file') # Arrumar
    print('[8] - Load a file') # Arrumar
    print('[9] - Exit')
    print('-' * 50)


def create_my_calendar(calendar) -> MyCalendar:
    if calendar is None:
        year = input('Enter the year: ')
        the_calendar = MyCalendar(int(year))
    else:
        confime_msg = 'You already have a MyCalendar,' \
                      'do you want to overwrite it? [Y/n]'

        res = input(confime_msg).lower()
        if res == 'y':
            year = input('Enter the year: ')
            the_calendar = MyCalendar(int(year))
        else:
            the_calendar = calendar
    return the_calendar


def create_task(calendar: MyCalendar):
    name = input('Task name: ')
    year = str(calendar.year)
    month = input('Task month MM: ')
    day = input('Task day DD: ')
    describe = input('Task describe: ')
    date = year + '/' + month + '/' + day
    calendar.create_task_in_month(name, date, describe)


def update_task(
        calendar: MyCalendar,
        id: int,
        month_number: int,
        name: str,
        month: str,
        day: str,
        describe: str
        ):
    month_task = calendar.months[month_number - 1]
    task = month_task.tasks[id - 1]
    year = str(calendar.year)
    date = year + '/' + month + '/' + day
    task.update_task(name, date, describe)


def finish_task(calendar: MyCalendar,
                id: int,
                month_number: int):
    try:
        month_task = calendar.months[month_number - 1]
        task = month_task.tasks[id - 1]
        task.finish_task()
    except IndexError:
        print('Id is out range')


def delete_task(calendar: MyCalendar,
                id: int,
                month_number: int):
    month_task = calendar.months[month_number - 1]
    try:
        task = month_task.tasks.pop(id - 1)
        print('WAS REMOVED: ', task)
    except IndexError:
        print('TASK LIST IS EMPTY')


def clear():
    os.system('clear')


if __name__ == '__main__':
    my_calendar = None
    enter_continue = 'Press Enter to continue'
    while True:
        clear()
        menu()
        res = input('>>> ')
        if res == '1':
            # Create MyCalendar
            my_calendar = create_my_calendar(my_calendar)
        elif res == '2':
            # Show MyCalendar
            if my_calendar is None:
                print('Create a MyCalendar first')
            else:
                my_calendar.show_calendar()
        elif res == '3':
            # Create Task
            if my_calendar is None:
                print('Create a MyCalendar first')
            else:
                create_task(my_calendar)
        elif res == '4':
            # Update Task
            id = int(input('Enter ID: '))
            month_number = int(input('Enter month number: '))
            name = input('Enter new name: ')
            month = input('Enter new month MM: ')
            day = input('Enter new day DD:')
            describe = input('Enter new describe: ')
            update_task(my_calendar, id, month_number,
                        name, month, day, describe)
        elif res == '5':
            # Finish a Task
            id = int(input('Enter Task ID: '))
            month_number = int(input('Enter month number: '))
            finish_task(my_calendar, id, month_number)
        elif res == '6':
            # Delete a Task
            id = int(input('Enter Task ID: '))
            month_number = int(input('Enter month number: '))
            delete_task(my_calendar, id, month_number)
        elif res == '7':
            # Save in file
            if my_calendar is None:
                print('Create a MyCalendar first')
            else:
                path = input('Enter with file name: ')
                my_calendar.save_in_file(path)
        elif res == '8':
            # Load a file
            if my_calendar is not None:
                confime_msg = 'You already have a MyCalendar,' \
                      'do you want to overwrite it? [Y/n]'
                res = input(confime_msg).lower()
                if res == 'y':
                    res = input('Enter with file name: ')
                    my_calendar = MyCalendar.load_file(res)
            else:
                res = input('Enter with file name: ')
                my_calendar = MyCalendar.load_file(res)
        elif res == '9':
            # Exit
            break
        else:
            print('Invalid option...')
            print('Please, enter with a valid option')
        input(enter_continue)
