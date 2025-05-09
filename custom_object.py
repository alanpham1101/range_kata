from abc import ABC, abstractmethod
from datetime import datetime, date


class CustomObject(ABC):
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __ge__(self, other):
        pass

    @staticmethod
    def get_lowest_bound(self):
        pass

    @staticmethod
    def get_uppermost_bound(self):
        pass


class IntObject(CustomObject, int):
    @staticmethod
    def get_lowest_bound() -> 'int':
        return -2**31

    @staticmethod
    def get_uppermost_bound() -> 'int':
        return 2**31 + 1


class FloatObject(CustomObject, float):
    @staticmethod
    def get_lowest_bound() -> 'float':
        return float("-inf")

    @staticmethod
    def get_uppermost_bound() -> 'float':
        return float("inf")


class CharObject(str):
    @staticmethod
    def get_lowest_bound() -> 'DatetimeObject':
        return 'a'

    @staticmethod
    def get_uppermost_bound() -> 'DatetimeObject':
        return 'z'


class DatetimeObject(CustomObject):
    def __init__(self, iso_date):
        dt = datetime.strptime(iso_date, "%Y-%m-%d")
        self.year = dt.year
        self.month = dt.month
        self.day = dt.day

    def __eq__(self, other: 'DatetimeObject'):
        return (
            self.year == other.year and
            self.month == other.month and
            self.day == other.day,
        )

    def __lt__(self, other: 'DatetimeObject'):
        return (
            self.year < other.year or
            (self.year == other.year and self.month < other.month) or
            (self.year == other.year and self.month == other.month and self.day < other.day)
        )

    def __gt__(self, other: 'DatetimeObject'):
        return (
            self.year > other.year or
            (self.year == other.year and self.month > other.month) or
            (self.year == other.year and self.month == other.month and self.day > other.day)
        )

    def __le__(self, other: 'DatetimeObject'):
        return (
            self.year <= other.year and
            self.month <= other.month and
            self.year <= other.year
        )

    def __ge__(self, other: 'DatetimeObject'):
        return (
            self.year >= other.year and
            self.month >= other.month and
            self.year >= other.year
        )

    @staticmethod
    def get_lowest_bound() -> 'DatetimeObject':
        return DatetimeObject(date.min.strftime("%Y-%m-%d"))

    @staticmethod
    def get_uppermost_bound() -> 'DatetimeObject':
        return DatetimeObject(date.max.strftime("%Y-%m-%d"))
