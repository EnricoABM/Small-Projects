"""Classes for Command-Line-Calendar

This module contain the classes to create Command-Line-Calendar
"""

from datetime import datetime
import calendar as cal
import locale
import json

# Set the locale to calendar
locale.setlocale(locale.LC_ALL, '')


class Task:
    def __init__(self, name: str, finish_date: str, describe: str) -> None:
        """Create tasks

        :param name: Task name
        :param finish_date: Finish date to complete task, it needs to be in
        this format (YYYY/MM/DD)
        :param describe: Describe of task
        """
        self.name = name
        self.finish_date = finish_date
        self.describe = describe
        self.status = False

    @property
    def finish_date(self):
        return self._finish_date

    @finish_date.setter
    def finish_date(self, value):
        self._finish_date = datetime.strptime(value, '%Y/%m/%d')

    def finish_task(self) -> None:
        """Complete a task, change the status to True"""
        if self.status:
            print('The task has already been completed')
            return None
        self.status = True

    def update_task(
            self, name: str = '',
            finish_date: str = '',
            describe: str = ''
            ) -> None:
        """Update tasks attributes

        :param name: Task name
        :param finish_date: Finish date to complete task, it needs to be in
        this format (YYYY/MM/DD)
        :param describe: Describe of task
        """
        if name:
            self.name = name
        if finish_date:
            self.finish_date = finish_date
        if describe:
            self.describe = describe

    def __repr__(self) -> str:
        date = self.finish_date.strftime('%Y/%m/%d')
        return f'{date} - {self.name} - {self.status}\n{self.describe}'


class Month:
    def __init__(self, number: int, year: int):
        """Create a month

        :param name: attributes"""
        self.name = cal.month_name[number]
        self.number = number
        self.year = year
        self.calendar = cal.month(self.year, self.number)
        self.tasks: list[Task] = []

    def add_tasks(self, *args):
        """Add a task in the list of tasks

        :param args: list of Tasks"""
        for item in args:
            if isinstance(item, Task):
                self.tasks.append(item)

    def create_task(self, name: str, finish_date: str, describe: str):
        """Create tasks for the month

        :param name: Task name
        :param finish_date: Finish date to complete task, it needs to be in
        this format (YYYY/MM/DD)
        :param describe: Describe of task
        """
        task = Task(name, finish_date, describe)
        self.add_tasks(task)

    def show_month(self):
        """Show the month with all tasks"""
        print()
        print(self.calendar)
        print('TASKS:')
        for i, task in enumerate(self.tasks):
            print(f'{i+1} - {task}')
        print()

    def __repr__(self) -> str:
        return f'{self.year} - {self.name}'


class MyCalendar:
    def __init__(self, year: int):
        """Create a calendar with months

        :param year: Calendar year"""
        self.year = year
        self.months = self.create_months()

    def create_months(self) -> list[Month]:
        months = []
        for month_number in range(1, 13):
            month = Month(month_number, self.year)
            months.append(month)
        return months

    def search_month(self, month_number: int):
        for month in self.months:
            if month.number == month_number:
                chossed_month = month
        return chossed_month

    def create_task_in_month(
            self,
            name: str,
            finish_date: str,
            describe: str
            ):
        data = finish_date.split('/')
        year, month, *_ = list(map(int, data))
        month_searched = self.search_month(month)

        if month_searched.year == year:
            month_searched.create_task(name, finish_date, describe)
        else:
            print('The year in task is not same of the MyCalendar')

    def show_calendar(self):
        """Show the calendar with all months"""
        for month in self.months:
            print('-' * 70)
            month.show_month()

    def save_in_file(self, path: str):
        with open(path, 'a') as file:
            json.dump(self.__dict__, file)

    @classmethod
    def load_file(cls, path: str):
        with open(path, 'r') as file:
            instancia = cls(2023)
            instancia.__dict__ = json.load(file)
            return instancia


if '__main__' == __name__:
    d1 = datetime(2023, 11, 10)
    print(type(d1.year))
