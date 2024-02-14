"""Classes for Command-Line-Calendar;

This module contain the classes to create Command-Line-Calendar;
"""

from datetime import datetime
from enum import Enum
import calendar as cal
import locale


# Set the locale to calendar
locale.setlocale(locale.LC_ALL, '')


class EnumStatus(Enum):
    TODO = 'To do'
    DONE = 'Done'


class Task:
    def __init__(
            self,
            name: str,
            year: int,
            month: int,
            day: int,
            describe: str) -> None:
        """Create a task;

        :param name: Task name;
        :param year: The year of the task to create datetime;
        :param month: The month of the task to create datetime;
        :param day: The day of the task to create datetime;
        :param describe: Describe of task;
        """
        self.name = name
        self.date = datetime(year, month, day)
        self.describe = describe
        self.status = EnumStatus.TODO.value

    def finish(self) -> None:
        """Complete a task, change the status to Done;"""
        if self.status == 'Done':
            print('The task has already been completed')
            return None
        self.status = EnumStatus.DONE.value

    def update(
            self,
            name: str = '',
            month: int = 0,
            day: int = 0,
            describe: str = '') -> None:
        """ Update tasks attributes;

        :param name: Task name;
        :param month: New month for the task;
        :param day: New day for the task;
        :param describe: Describe of task;
        """
        if name:
            self.name = name

        if month:
            self.date = self.date.replace(month=month)

        if day:
            self.date = self.date.replace(day=day)

        if describe:
            self.describe = describe

    def __repr__(self) -> str:
        date = self.date.strftime('%Y/%m/%d')
        return f'{date} - {self.name} - {self.status}\n{self.describe}'


class Month:
    def __init__(self, number: int, year: int):
        """Create a month;

        :param number: Month number;
        :param year: Year of the month;
        """
        self.name = cal.month_name[number]
        self.number = number
        self.year = year
        self.calendar = cal.month(self.year, self.number)

    def show_month(self):
        """Show the calendar month; """
        print(self.calendar)

    def __repr__(self) -> str:
        return f'{self.year} - {self.name}'


class MyCalendar:
    def __init__(self, year: int):
        """Create a calendar with months and tasks;

        :param year: Calendar year;
        """
        self.year = year
        self.months = self.__create_months()
        self.tasks: list[Task] = []

    def __create_months(self) -> list[Month]:
        months = []
        for month_number in range(1, 13):
            month = Month(month_number, self.year)
            months.append(month)
        return months

    def create_task(
            self,
            name: str,
            month: int,
            day: int,
            describe: str
            ):
        if month > 12:
            month = 12
        elif month < 1:
            month = 1

        last_day_month = cal.monthrange(self.year, month)

        if day > last_day_month[1]:
            day = last_day_month[1]
        elif day < 1:
            day = 1

        self.tasks.append(Task(name, self.year, month, day, describe))

    def show_calendar(self):
        """ Show the calendar with all months; """
        for month in self.months:
            print('-' * 50)
            month.show_month()
            print('-' * 50)
            print('TASK(S):\n')
            for id, task in enumerate(self.tasks):
                if month.number == task.date.month:
                    print(id, task)

    def show_month(self, month_number: int):
        """! Show a specific month calendar; """
        print('-' * 50)
        self.months[month_number - 1].show_month()
        print('-' * 50)
        print('TASK(S):\n')
        for id, task in enumerate(self.tasks):
            if task.date.month == month_number:
                print(id, '-', task)

    def update_task(
            self,
            id: int,
            name: str,
            month: int,
            day: int,
            describe: str):
        if id > len(self.tasks):
            print('Id out of range')
            return
        task = self.tasks[id]
        task.update(name, month, day, describe)

    def finish_task(self, id: int):
        if id > len(self.tasks):
            print('Id out of range')
            return
        task = self.tasks[id]
        task.finish()

    def delete_task(self, id: int):
        if id > len(self.tasks):
            print('Id out of range')
            return
        item = self.tasks.pop(id)
        print('This task is removed:', item)

    def show_all_tasks(self):
        for id, task in enumerate(self.tasks):
            print(id, '-', task)

    def __repr__(self) -> str:
        return f'calendar: {self.year} with {len(self.tasks)} task(s)'

    def load_data(self):
        data = {**self.__dict__}
        months = []
        tasks = []
        for month in data['months']:
            months.append(month.__dict__)

        for task in data['tasks']:
            tasks.append(task.__dict__)

        data['months'] = months
        data['tasks'] = tasks

        for task in data['tasks']:
            data_dct = dict(
                month=task['date'].month,
                day=task['date'].day)
            task['date'] = data_dct
        return data

    def restore_data(self, data: dict):
        self.year = data['year']
        for value in data['tasks']:
            self.tasks.append(
                Task(
                    value['name'],
                    self.year,
                    value['date']['month'],
                    value['date']['day'],
                    value['describe']
                )
            )
        self.months = self.__create_months()


if '__main__' == __name__:
    m1 = MyCalendar(2023)
    m2 = MyCalendar(2020)
    m1.create_task('1', 1, 1, '1')
    m1.create_task('2', 1, 1, '2')
    m1.create_task('3', 1, 1, '3')
    m1.create_task('4', 1, 1, '4')
    m1.create_task('5', 1, 1, '5')
    m1.create_task('6', 1, 1, '6')
